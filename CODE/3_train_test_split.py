# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:37:05 2022

@author: arunkumar.b
"""

from tkinter import filedialog
import tkinter
tkinter.Tk().withdraw()
import os
import random
import shutil


#%%
print ("SELCET FOLDER WHERE DATA is available")
raw_data = filedialog.askdirectory()
print ("SELECTED FOLDER\t:\t",raw_data)

print ("No of data for train & No of data for test")
train    =int(input())
test   =int(input())

print ("SELCET FOLDER WHERE COPY TEST\TRAIN")
output = filedialog.askdirectory()
print ("SELECTED FOLDER\t:\t",output)
#%%
if not  os.path.isdir(output+"/test"):
    os.makedirs(output+"/test")
    if not  os.path.isdir(output+"/train"):
        os.makedirs(output+"/train")
#%%
print ("\n\nPROCESS STARTED")
print ("-------------------")
print ("INPUT FOLDER\t:\t",raw_data)
print ("OUTPUT FOLDER\t:\t",output)
print ("Checking Content in the folder")
for i in os.listdir(raw_data):
    print ("\n\nCURRENT FOLDER-->",i)
    res = random.sample(range(0, 11), train)
    print ("TRAIN DATA")
    for j in res:
        jpeg_path=raw_data+"/"+str(i)+"/"+str(i)+"_"+str(j)+".jpg"
        xml_path =raw_data+"/"+str(i)+"/"+str(i)+"_"+str(j)+".xml"
        print (jpeg_path)
        shutil.copy(jpeg_path, output+"/train/")
        shutil.copy(xml_path, output+"/train/")
    print ("TEST DATA")
    for ij in range(0,11):
        if ij not in res:
            jpeg_path=raw_data+"/"+str(i)+"/"+str(i)+"_"+str(ij)+".jpg"
            xml_path =raw_data+"/"+str(i)+"/"+str(i)+"_"+str(ij)+".xml"
            print (jpeg_path)
            shutil.copy(jpeg_path, output+"/test/")
            shutil.copy(xml_path, output+"/test/")

#%%