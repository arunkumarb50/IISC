# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:06:38 2022

@author: arunkumar.b
"""
#%% LIBRARY INSTALLATION
# This code is made to collect data from the camera and save to respective Folder
# Folder for save,number of data can be configure and auto  named
import cv2
import tkinter
from tkinter import filedialog
tkinter.Tk().withdraw()
import os
import time
#%%
vid = cv2.VideoCapture(1)
print("SELECT Folder to Save image") 
image_path = filedialog.askdirectory()
print ("SELECTED FOLDER\t:\t",image_path)
print ("Enter name of class")
name=input()
image_path=image_path+"/"+name
if not  os.path.isdir(image_path):
    os.makedirs(image_path)
#%%
for i in range(0,5):
    print ("press s to save image \t:\t",i+1)
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('s'):
            print("Trigger to capture image")
            cv2.imwrite(image_path+"/"+name+"_"+str(i)+".jpeg",frame)
            time.sleep(2)
            break
        if i>4:
            break
        time.sleep(0.1)
vid.release()
cv2.destroyAllWindows()