# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:48:29 2022

Plots for volume and pressure relationship against time relationship
Data from pressure from previous experiments and data for volume extracted from video frame clickpoints
Data as used is Current proportional to pressure and Diameters/Lengths proportional to cube root of volume in pixels
Pixels could be coverted to metric/imperial unit with pixel per meter constant considering diameter of pressure gauge in video is 5in

@author: Godswill Agbofode
"""

import cv2     # for capturing videos
import math   # for mathematical operations
import matplotlib.pyplot as plt 
import sys   # for plotting the images
#%matplotlib inline
import pandas as pd
#from keras.preprocessing import image   # for preprocessing the images
import numpy as np    # for mathematical operations

d_p= pd.read_excel("D:\\Documents\\Documents\\McGill School Documents\\1.)Winter_2022\\MECH 403_ THESIS\\20200309-1354-vvb3_for_python_a1.xlsx")
d_p.head()
#Headings: 'Time(ms)' , 'Current_0' , 'Current_1'
#print(d_p['Time(ms)'])

#%%

d_v=pd.read_excel("D:\\Documents\\Documents\\McGill School Documents\\1.)Winter_2022\\MECH 403_ THESIS\\test_d4.xlsx")
d_v.head()
#Headings: 'Time(in milliseconds)' , 'D1' , 'D2' , 'D3' , 'V1', 'V2'
#print(d_v)


#%%
fig, ax = plt.subplots()
ax.set_xlabel(r'$t$ (s)')
ax.set_ylabel(r'$Pressure$, $Volume$, $Scaled to fit (units)')
#plt.xlim(-5, 22)
#plt.ylim(-25, 15)
# Plot data
#Plot Pressures/Currents
#%%
ax.plot(d_p['Time(ms)'], d_p['Current_0'], label='$Pressure 0$', color='C0')
ax.plot(d_p['Time(ms)'], d_p['Current_1'], label='$Pressure 1$', color='C1')

#%%
ax.plot(d_v['Time(in_milliseconds)'], (d_v['V1']/1000000), label='$Volume 0$', color='C2')
ax.plot(d_v['Time(in_milliseconds)'], (d_v['V2']/1000000), label='$Volume 1$', color='C3')
ax.legend(loc='upper right')
fig.tight_layout()
plt.show()
