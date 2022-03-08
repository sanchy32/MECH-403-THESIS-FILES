#====================================
#Acknowledgment Info: To be added
#==============================
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
videoFile = '20200309-1354-vvb3.mp4'
cap = cv2.VideoCapture('20200309-1354-vvb3.mp4')   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
print(cap.isOpened())
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    print('Hello')
    ret, frame = cap.read()
    if (ret != True):
        print("Is not true")
        break
    print('Bye')
    if (frameId % math.floor(frameRate) == 0):
        filename ="frame%d.jpg" % count;count+=1
        cv2.imwrite(filename, frame)
cap.release()
print ("Done!")

#%%
img = plt.imread('frame0.jpg')   # reading image using its name
plt.imshow(img)
#%%Label Images
# data = pd.read_csv('mapping.csv')     # reading the csv file
# data.head()      # printing first five rows of the file
# #Read Images
# X = [ ]     # creating an empty array
# for img_name in data.Image_ID:
#     img = plt.imread('' + img_name)
#     X.append(img)  # storing each image in array X
# X = np.array(X)    # converting list to array