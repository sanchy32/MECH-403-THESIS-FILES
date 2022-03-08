#Imports
import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt    # for plotting the images
#%matplotlib inline
import pandas as pd
#from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
#from keras.utils import np_utils
#from skimage.transform import resize   # for resizing images

#%%Read the video, extract frames from it and save 
# them as images
count = 0
#videoFile = "D:\Documents\Documents\McGill School Documents\1.)Winter_2022\MECH 513\Sequential auxetics video_v02.m4v"
cap = cv2.VideoCapture('20200309-1354-vvb3.mp4')   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
print(frameRate)
print(cap.isOpened())
#%%
x=1
while(True):
    print('hello')
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        print("Is not true")
        break
    print('Bye')
    if (frameId % math.floor(frameRate) == 0):
        #filename ="" % count
        cv2.imwrite(f'frame_{count}.jpg', frame);count+=1
cap.release()
print ("Done!")

#%%
img = plt.imread('D:\Documents\Documents\McGill School Documents\1.)Winter_2022\MECH 513\frame_0.jpg')   # reading image using its name
plt.imshow(img)
