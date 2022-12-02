# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:48:29 2022

Plots for volume and pressure relationship against time relationship
Data from pressure from previous experiments and data for volume extracted from video frame clickpoints
Data as used is Current proportional to pressure and Diameters/Lengths proportional to cube root of volume in pixels
Pixels could be coverted to metric/imperial unit with pixel per meter constant considering diameter of pressure gauge in video is 5in

Edited on Mon Mar 18 14:44 2022, A2.
Plot drawstyle set to step.
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
from tkinter.filedialog import askopenfilename
video_name = askopenfilename()
# =============================================================================
# d_p= pd.read_excel("D:\\Documents\\Documents\\McGill School Documents\\1.)Winter_2022\\MECH 403_ THESIS\\20200309-1354-vvb3_for_python_a1.xlsx")
# d_p.head()
#=============================================================================
#Headings: 'Time(ms)' , 'Current_0' , 'Current_1'
#print(d_p['Time(ms)'])


#%%Parameters
#filename = input("Enter excel file name")

theta = 78
tantheta = math.tan(39 * (math.pi/180))

h= 1280 #height_in_pixels 1980
w = 720 #width_in_pixels 1080

V = 37 

#init = ?

SFac = 2.54 #Initial width diameter of bubble in cm
#d_v=pd.read_excel("D:\\Documents\\Documents\\McGill School Documents\\1.)Winter_2022\\MECH 403_ THESIS\\20200203_VCchamber_Spinchpoints-2.xlsx")
d_v=pd.read_excel(video_name)
init = (d_v['D1'].iloc[1])
c = SFac/init

denom = c * (math.sqrt((w**2)+(h**2)))*tantheta
#print(denom)
#%%
SFac = SFac/(d_v['D1'].iloc[1])
d_v.head()
#Headings: 'Time(in milliseconds)' , 'Dh1' , 'Dv1, 'Dh2' , 'Dv2', 'Dh3' , 'Dv3'

#%%
# =============================================================================
# fig, ax = plt.subplots()
# ax.set_xlabel(r'$t$ (s)', fontsize='12')
# ax.set_ylabel(r'$Diameter\;(cm)$', fontsize='12')
# ax.plot(d_v['Time(in milliseconds)']/1000, (d_v['Dh1'])*SFac, drawstyle = 'steps-post', label='$Dh1$', color='black')
# ax.plot(d_v['Time(in milliseconds)']/1000, (d_v['Dh2'])*SFac, drawstyle = 'steps-post', label='$Dh2$', color='red')
# ax.plot(d_v['Time(in milliseconds)']/1000, (d_v['Dh3'])*SFac, drawstyle = 'steps-post', label='$Dh3$', color='blue')
# lines, labels = ax.get_legend_handles_labels() 
# ax.legend(lines, labels, loc='upper left', fontsize ='12')
# fig.tight_layout()
# plt.show()
# fig.savefig('20200203_VCchamber_Spinchpoints-2_Hor_D.jpeg', format='pdf')
# =============================================================================

#plt.xlim(240, 420)
#plt.ylim(-25, 15)
# Plot data
#Plot Pressures/Currents

#%%
#ax2 = ax.twinx()
#ax.set_ylabel(r'$Volume\;(Proportional\;to\;Pixels\;(CentiPixels))$', fontsize = '12')#', $Volume$, $Scaled to fit (units)'

#(d_v['D1']*c)-(d_v['D1']*c*((c*(d_v['D1']-init)/2)/denom))

fig, ax2 = plt.subplots()
ax2.set_xlabel(r'$t$ (s)', fontsize='12')
ax2.set_ylabel(r'$Volume\;Proportion\;(cm^3)$', fontsize='12')

ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D1']*c)**3-3*((d_v['D1']*c)**2)*(d_v['D1']*c*((c*(d_v['D1']-init)/2)/denom)), yerr = 3*((d_v['D1']*c)**2)*(d_v['D1']*c*((c*(d_v['D1']-init)/2)/denom)), label='$D1$', color='black')
ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D2']*c)**3-3*((d_v['D2']*c)**2)*(d_v['D2']*c*((c*(d_v['D2']-init)/2)/denom)), yerr = 3*((d_v['D2']*c)**2)*(d_v['D2']*c*((c*(d_v['D2']-init)/2)/denom)), label='$D2$', color='red')
ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D3']*c)**3-3*((d_v['D3']*c)**2)*(d_v['D3']*c*((c*(d_v['D3']-init)/2)/denom)), yerr = 3*((d_v['D3']*c)**2)*(d_v['D3']*c*((c*(d_v['D3']-init)/2)/denom)), label='$D3$', color='blue')

# =============================================================================
# ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D1']*c)**3-3*((d_v['D1']*c)**2)*(d_v['D1']*c*((c*(d_v['D1']-init)/2)/denom)), yerr = 3*((d_v['D1']*c)**2)*(d_v['D1']*c*((c*(d_v['D1']-init)/2)/denom)), drawstyle = 'steps-post', label='$D1$', color='black')
# ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D2']*c)**3-3*((d_v['D2']*c)**2)*(d_v['D2']*c*((c*(d_v['D2']-init)/2)/denom)), yerr = 3*((d_v['D2']*c)**2)*(d_v['D2']*c*((c*(d_v['D2']-init)/2)/denom)), drawstyle = 'steps-post', label='$D2$', color='red')
# ax2.errorbar(d_v['Time(in milliseconds)']/1000, (d_v['D3']*c)**3-3*((d_v['D3']*c)**2)*(d_v['D3']*c*((c*(d_v['D3']-init)/2)/denom)), yerr = 3*((d_v['D3']*c)**2)*(d_v['D3']*c*((c*(d_v['D3']-init)/2)/denom)), drawstyle = 'steps-post', label='$D3$', color='blue')
# =============================================================================
lines, labels = ax2.get_legend_handles_labels() 
ax2.legend(lines, labels, loc='upper left', fontsize ='12')
fig.tight_layout()
plt.show()
fig.savefig(video_name + '.pdf', format='pdf')


