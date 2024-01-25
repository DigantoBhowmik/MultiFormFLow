from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_user, name='form'),
    path('get/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
]
