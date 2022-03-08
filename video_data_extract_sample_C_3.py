"""
Created on Fri Feb 11 15:14:18 2022

@author: Godswill Agbofode
Reference: To be added
    """
#Imports
import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt 
import sys   # for plotting the images
#%matplotlib inline
import pandas as pd
#from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations
#from keras.utils import np_utils
#from skimage.transform import resize   # for resizing images
#send output to textfile
sys.stdout = open("test_d3.txt", "w")
#%%Introduce clicking functionality
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(str(count)+ ', '+ str(cap.get(0))+', ' + str(x), ', ', str(y),)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
#%%Read the video, extract frames from it and save 
# them as images
count = 0
#videoFile = "D:\Documents\Documents\McGill School Documents\1.)Winter_2022\MECH 513\Sequential auxetics video_v02.m4v"
cap = cv2.VideoCapture('20200309-1354-vvb3.mp4')   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
#print("The framerate is " + str(frameRate))
#print("The cap is opened: " + str(cap.isOpened()))
#%%
print('Frame ID, Time(in milliseconds), X-coord, Y-coord')
x=1
while(True):
    #print('hello')
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        #print("Is not  ")
        break
    #print('Bye')
    if(cap.get(0)<((4*60+25)*1000)):
        #print('Time in ms: ' + str(cap.get(0)) +', Frame ID: ' + str(frameId) + ', Rel Pos: '+ str(cap.get(2)))
        continue
    if (frameId % math.floor(frameRate) == 0):
            #filename ="" % count
            #print('Stuff happens')
            #print('Time in ms: ' + str(cap.get(0)) +', Frame ID: ' + str(frameId) + ', Stuff happens')
           
            ###Introduce clicking 
            
           if __name__=="__main__":
             
                # reading the image
                #img = cv2.imread(frame)
                img = frame 
                # displaying the image
                cv2.imshow('image', img)
             
                # setting mouse handler for the image
                # and calling the click_event() function
                cv2.setMouseCallback('image', click_event)
             
                # wait for a key to be pressed to exit
                cv2.waitKey(0)
             
                # close the window
                cv2.destroyAllWindows()
            #cv2.imwrite(f'frame_{count}.jpg', frame)
                count+=1
cap.release()
sys.stdout.close()
print ("Done!")

#%%
#img = plt.imread('frame_28.jpg')   # reading image using its name
#plt.imshow(img)
