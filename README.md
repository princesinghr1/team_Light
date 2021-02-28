a:Title:

We have created 2 modules
1:Lift
2:Cursor

Both of these modules work on a real-time gesture bases that means without user's interaction with keypad and mouse

b:Description:

According to current evidence, COVID-19 virus is primarily transmitted between people through respiratory droplets and contact routes. During this pandemic situation, it is advised to have less human contact as much as possible.
So we present an application of neural networks and image processing techniques.

I:In our first module 'Lift' user will show the direction either "upwards" or "downwards" thereafter selecting the direction he will metions the floor number and this is how the lift will operate.

Algorithm for module Lift:

For identification of hand gestures, we used a 1D convolution neural network. Our task involved identifying gestures that represent both alphabetic and numeric characters, but there are some characters that are common in both. To solve that problem we created some of our own custom gestures. Once we created the dataset, we took the coordinates of the landmarks of the hand.


Step 1: First we will capture the video and will pass the frames through our application .Our application will give the coordinates of the given 21 landmarks

Step 2: Once we get the coordinates, we subtract them with the coordinates for ‘0’ landmark. This way our hand is always shifted to origin irrespective of where it is placed on screen. These coordinates are stored in a .csv format which are later used for training.
	Shifted_coordinates =  original_coordinates - origin
Step 3: For training of the model, we used a simple convolution neural network. Since we are dealing with coordinates of the landmark and not actual image, We used 1 dimensional convolution and max pooling filters.

Step 4: Input layer consists of all coordinates  of the 21 landmarks  in 3 dimensions(x,y,z). We do not include ‘0’ landmark as it will always be (0,0,0).

Step 5: In this way we have trained our dataset and applied on test inputs by which we can able to recognize the gesture and able to manage passwords.



II:In the second module 'Cursor' user can control the entire screen by operation like click,move and double-click.This means without interacting with mouse or any external device he can control the screen.

Algorithm for Cursor module:

Step 1: First we will capture the video and will pass the frames through our application .Our application will give the coordinates of the given 21 landmarks

Step 2:Among all the 21 landmark we are extracting only the first finger landmark and using its co-ordinates(x and y)

Step 3:Synchronizing with on screen cursor using Mapping
Forming mathematical relationship for mapping 

Step 4:Once the mouse is synchronized then using different gestures for operations like click,move and double-click 



C:Tech Stack

Live video feed is acquired using the device camera itself. OpenCV (Open Source Computer Vision Library)  library is used for real-time computer vision.
You can use get(CAP_PROP_FPS) or get(CV_CAP_PROP_FPS) to get frames per second. 
A Video is made up of multiple still images known as Frames, 60 FPS means there are 60 images per second of video. All images are passed through Mediapipe.
Image Acquisition is done in real-time, and sent to mediapipe library(An open source google library) for the coordinates then passed through deep learning to get the Gesture



