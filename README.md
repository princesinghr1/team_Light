## Title
`Contactless Lifestyle`

## Description
We have created 2 modules
* `Lift` (Module for elevators) 
* `Cursor` (Module for using machines such as ATMs and vending machines)

These modules are both gesture controlled and does not require any physical contact. 


### Need for the project
According to current evidence, COVID-19 virus is primarily transmitted between people through respiratory droplets and contact routes. During this pandemic situation, it is advised to have less human contact as much as possible.
So we present an application of neural networks and image processing techniques to enable people to use gestures to operate the public machines that traditionally required physical contact.

<b>In our first module 'Lift' user will show the direction either "upwards" or "downwards" thereafter selecting the direction he will mention the floor number and this is how the lift will operate.</b>

Algorithm for module Lift

For identification of hand gestures, we used a 1D convolution neural network. To solve that problem we created some of our own custom gestures. Once we created the dataset, we took the coordinates of the landmarks of the hand for training the network.


1. First we will capture the video and will pass the frames through our application. Our application will give the coordinates of the given 21 landmarks

2. Once we get the coordinates, we subtract them with the coordinates for `0` landmark. This way our hand is always shifted to origin irrespective of where it is placed on screen. These coordinates are stored in a .csv format which are later used for training.
	`Shifted_coordinates =  original_coordinates - origin`
3. For training of the model, we used a simple convolution neural network. Since we are dealing with coordinates of the landmark and not actual image, We used 1 dimensional convolution and max pooling filters.

4. Input layer consists of all coordinates  of the 21 landmarks  in 3 dimensions(x,y,z). We do not include `0` landmark as it will always be (0,0,0).

5. In this way we have trained our dataset and applied on test inputs by which we are able to recognize the gesture to operate the lift.



<b>In the second module 'Cursor' user can control the entire screen by operation like click,move and double-click.This means without interacting with mouse or any external device he can control the screen.</b>

Algorithm for Cursor module

1. First we will capture the video and will pass the frames through our application. Our application will give the coordinates of the given 21 landmarks

2. Among all the 21 landmark we are extracting only the first finger landmark and using its co-ordinates(x and y)

3. We mapped the relationship between the displacement of the finger and the displacement of the cursor on the screen.

4. Once the mouse is synchronized then using different gestures for operations like click,move and double-click 


## Application
### Lift (Elevator)
1. We can operate the elevator without physically pressing the button hence avoiding the contact.
2. The hack does not use any special device from the user side to function

### Cursor 
1. It can be used to operate any device with camera instead of a keypad
2. The speed and accuracy of taking the input and recognizing gestures makes it a viable alternative to keypad operated devices.


## Tech Stack
Live video feed is acquired using the device camera itself. OpenCV (Open Source Computer Vision Library)  library is used for real-time computer vision.
You can use get(CAP_PROP_FPS) or get(CV_CAP_PROP_FPS) to get frames per second. 
A Video is made up of multiple still images known as Frames, 60 FPS means there are 60 images per second of video. All images are passed through Mediapipe.
Image Acquisition is done in real-time, and sent to mediapipe library(An open source google library) for the coordinates then passed through deep learning to get the Gesture.



## Libraries and dependencies required for the project (If any)
Hack uses python with opencv,mediapipe,numpy,pandas,keras

## Installation steps: A clear sequence of steps to run your hack
Download Python from : https://www.python.org/

Once python is installed run
`pip install requirements.txt`

<b> Runnning Elevator </b> 
1. change directory to Hackverse/Lift using `cd Hackverse/Lift`
2. Run `python main.py`

<b> Running Cursor </b>
1. change directory to Hackverse/Cursor using `cd Hackverse/Cursor`
2. Run `Cursor.ipynb`

## Declaration of Previous Work
We had implemented the similar method for recognising the American sign language. In this project we have modified the application for Lift Module. And used the landmark acqusitions as same as before for the Cursor. However in the cursor we have added the stabelizing and mapping functions and added cursor control to it.

