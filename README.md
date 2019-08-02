# Autonomous-Driving-Using-CNN

This project comprises of a simulated environment "Road Network" built with Unity3D and a Convolutiuonal Neural Network that is trained to drive a car autonomously on this environment.

![Cover Photo](https://github.com/BharathRajM/Autonomous-Driving-Using-CNN/blob/master/Images/CoverPhoto1.png)

Introduction
In this project we train a car in a simulated environment to safely navigate itself. The approach is to make use of a Convolutional Neural Network.

Technical details - 
Here I make use of Unity3D to develop the environment and Python to write our machine learning scripts.

The dataset for our CNN is built by taking instances of actions[steer left,accelerate,reverse,steeer right,take no action] and their respective image frames.

![](https://github.com/BharathRajM/Autonomous-Driving-Using-CNN/blob/master/Images/synopsis%20photo.png)

## Workflow

The camera feed and the respective action of this frame is sent to a CNN.
By making enough number of image and action pairs we build our dataset and train on an AlexNet.

![](https://github.com/BharathRajM/Autonomous-Driving-Using-CNN/blob/master/Images/alexnet.png)

![](https://github.com/BharathRajM/Autonomous-Driving-Using-CNN/blob/master/Images/workflow.png)

## Collection of the dataset
The dataset was created by playing the game numerous hours and accounting the keystrokes which each image frame. These were stored in a 2-dimensional array format in numpy, where the array[0] contained the image frame pixel values in grayscale and the array[1] contained the corresponding keystroke. There are about 40-45 thousand samples each of them are of the dimension –
[160 pixels X 120 pixels X 1 grayscale channel] X [ particular keystroke(a,w,s,d,'nothing')]

![](https://github.com/BharathRajM/Autonomous-Driving-Using-CNN/blob/master/Images/dataset.png)

## Results Achieved

The CNN manages to do a fairly remarkable job by classifying correctly as to what action needs to be taken –
1. Steer left
2. Accelerate
3. Steer right
4. Apply brakes
5. Take no action
Even when the car is set out of track, if there is a road present in the frame the CNN drives the vehicle towards the track, this is something surprising.
