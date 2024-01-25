from threading import Thread
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.http import HttpResponse
import numpy as np
from PIL import Image
import easyocr
from users.models import Users

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def get_user_by_email(request, email):
    user = Users.objects.filter(email=email).first()
    if user is not None:
        user_dict = model_to_dict(user)
        return JsonResponse(user_dict)
    else:
        return HttpResponse('null', content_type='text/plain')

@api_view(['POST'])
def create_user(request):
    try:
        data = request.data.dict()
        user, created = Users.objects.get_or_create(email=data['email'])

        if data['instraFile']:
            image_array = crop_image(data['instraFile'])
            return instra_ocr_perform(user, image_array)
            # thr = Thread(target=instra_ocr_perform, args=[user.email, image_array])
            # thr.start()
            
        if data['ytUsername']:
            if data['ytUsername'][0] != '@':
                data['ytUsername'] = '@' + data['ytUsername']
            checkytUsername = Users.objects.filter(yt_username=data['ytUsername']).first()
            if checkytUsername is not None and checkytUsername.email != user.email:
                # Return error message
                return Response({'message': 'This username has already exits. Please use a different username.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.yt_username = data['ytUsername']
            
        if data['ytcFile']:
            user.is_ytc_ss = True
            image_array = crop_image(data['ytcFile'])
            thr = Thread(target=check_is_comment, args=[user.email, image_array])
            thr.start()
            
        if data['ytUrl']:
            user.yt_url = data['ytUrl']

        user.save()
        user_dict = model_to_dict(user)
        return JsonResponse(user_dict)
    except Exception as e:
        return Response({'error': str(e)})

def crop_image(instraFile):
    original_image = Image.open(instraFile)
    # Get the dimensions of the original image
    width, height = original_image.size

    # Set the crop coordinates to remove the upper part (adjust the values as needed)
    top_crop = int(height * 0.05)
    bottom_crop = height   # Keep 80% of the original height

    # Crop the image
    cropped_image = original_image.crop((0, top_crop, width, bottom_crop))

    # Convert the PIL Image to a numpy array
    image_array = np.array(cropped_image)
    
    return image_array


def instra_ocr_perform(user,image_array):
    try:
        # Initialize the OCR reader
        reader = easyocr.Reader(['en'], gpu=False)  # this needs to run only once to load the model into memory

        # Read text from the image
        result = reader.readtext(image_array, detail=0)
        
        search_string = 'sadhguru'
        
        existUser = Users.objects.filter(instra_username=result[0]).first()
        
        if existUser is not None:
            # Return error message
            return Response({'message': 'A screenshot with this username has already been uploaded. Please use a different username.'}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            if 'No users found' in result:
                is_following = False
            elif search_string in result:
                index = result.index(search_string)
                is_following = 'Following' in result[index+1] or 'Following' in result[index+2]
            else:
                is_following = False
                
            # user = Users.objects.get(email=email)
            user.is_instra_ss = True
            user.is_following = is_following    
            user.instra_username = result[0]
            user.save()
            user_dict = model_to_dict(user)
            return JsonResponse(user_dict)
        
    except Exception as e:
        return Response({'error': str(e)})
    

def check_is_comment(email, image_array):
    try:
        # Initialize the OCR reader
        reader = easyocr.Reader(['en'], gpu=False)  # this needs to run only once to load the model into memory

        # Read text from the image
        result = reader.readtext(image_array, detail=0)
        
        user = Users.objects.get(email=email)
        found = user.yt_username in result
        
        user.is_comment = found
        user.save()
    except Exception as e:
        return print({'error': str(e)})

