# Multi-Step Form with Django and Angular
This is a client project that I received from Upwork. I have to create a multi-step form with Django and Angular. The form will collect data from users and validate the data. The form will have multiple steps and the user should be able to save the progress and continue later. The form will have the following steps:

#### Step 1: Setup Django Backend

1. Create a Django project and app.
2. Set up MongoDB for the Django project.
3. Define the necessary models to store email, screenshots, and validation status.

#### Step 2: Frontend with Angular

1. Create an Angular app for the frontend.
2. Design forms for each step (email, screenshots, and URL).
3. Implement the logic to send data to the Django backend.

#### Step 3: Email Validation

1. Implement email validation and storage in the database.
2. If the user closes the screen, save the progress to continue later.

#### Step 4: Instagram Screenshot

1. Show an example screenshot for Instagram.
2. Implement image upload, process using EasyOCR for text recognition.
3. Validate the Instagram username already store in database or not.
4. Validate that person actually follow their Id or not.

#### Step 5: YouTube Username Validation

1. Show an example screenshot for YouTube.
2. Implement image upload and processing using EasyOCR for text recognition.
3. Validate the YouTube username entered by the user.

    - **Check Database:** 
      - Verify if the entered YouTube username already exists in the database.
  
    - **Error Handling:**
      - If the username is not in the database, proceed to the next step.
      - If the username is already in the database, display an error message to the user.

#### Step 6: YouTube Comment Screenshot

1. Show an example screenshot for YouTube comments.
2. Implement image upload, process using EasyOCR for text recognition.
3. Validate if the entered YouTube username has a comment or not.

#### Step 7: URL Validation

1. Save the provided URL in the database.

#### Step 8: Database Integration

1. Establish a connection with MongoDB to store all the collected data.
2. Implement queries to check if the Instagram or YouTube username already exists in the database.

#### Step 9: Error Handling and User Messages

1. Display appropriate error messages for invalid data.
2. Record validation status in the database.

