# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:59:35 2022

@author: arunkumar.b
"""
import wget
import os
#%%

CUSTOM_MODEL_NAME       = 'my_ssd_mobnet' 
PRETRAINED_MODEL_NAME   = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8'
PRETRAINED_MODEL_URL    = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_RECORD_SCRIPT_NAME   = 'generate_tfrecord.py'
LABEL_MAP_NAME          = 'label_map.pbtxt'
#%%
paths = {
    'WORKSPACE_PATH': os.path.join('Tensorflow', 'workspace'),
    'SCRIPTS_PATH': os.path.join('Tensorflow','scripts'),
    'APIMODEL_PATH': os.path.join('Tensorflow','models'),
    'ANNOTATION_PATH': os.path.join('Tensorflow', 'workspace','annotations'),
    'IMAGE_PATH': os.path.join('Tensorflow', 'workspace','images'),
    'MODEL_PATH': os.path.join('Tensorflow', 'workspace','models'),
    'PRETRAINED_MODEL_PATH': os.path.join('Tensorflow', 'workspace','pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'export'), 
    'TFJS_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfjsexport'), 
    'TFLITE_PATH':os.path.join('Tensorflow', 'workspace','models',CUSTOM_MODEL_NAME, 'tfliteexport'), 
    'PROTOC_PATH':os.path.join('Tensorflow','protoc')
 }
files = {
    'PIPELINE_CONFIG':os.path.join('Tensorflow', 'workspace','models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}
for path in paths.values():
    if not os.path.exists(path):
        os.makedirs(path)
#%%INSTALLING TENSOR FLOW
# Go inside TENSORFLOW MODELS
# Open TERMINAL and CLONE MODEL FROM THE ONLINE
#git clone https://github.com/tensorflow/models
os.chdir('Tensorflow\\protoc')
url="https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip"
wget.download(url)
#unzip the file
#Go to the folder Tensorflow/models/research
# D:\PERSONAL\STUDY\IISC\Code\PROJECT\Quality\CODE\Tensorflow\protoc\bin  
# [protoc Full path] object_detection/protos/*.proto --python_out=.
#copy object_detection\\packages\\tf2\\setup.py setup.py 
#python setup.py build 
#python setup.py install
#Go to folder Tensorflow/models/research/slim 
#Run below command
#pip install -e . 
#%%
wget.download(PRETRAINED_MODEL_URL)
#UnZip
#Copy to TENSORFLOW PRETRAAINED MODE
#    !move {PRETRAINED_MODEL_NAME+'.tar.gz'} {paths['PRETRAINED_MODEL_PATH']}
#    !cd {paths['PRETRAINED_MODEL_PATH']} && tar -zxvf {PRETRAINED_MODEL_NAME+'.tar.gz'}
    
#%%
labels = [{'name':'CLAMP', 'id':1}, {'name':'COMPA', 'id':2}, {'name':'COMPB', 'id':3}, {'name':'SCREW', 'id':4}]

with open(files['LABELMAP'], 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')
#%%RUN THE BELOW CODE TO CHECK ALL OK
'Tensorflow\\models\\research\\object_detection\\builders\\model_builder_tf2_test.py'
#If it show OK THEN DEPENDENCY OVER
#%%
import object_detection
#%% Generating TF RECORD
#python file_name -x Tensorflow\\workspace\\images\\train
#                 -l Tensorflow\\workspace\\annotations\\label_map.pbtxt
#                 -o Tensorflow\\workspace\\annotations\\train.record'
##python file_name -x Tensorflow\\workspace\\images\\train -l Tensorflow\\workspace\\annotations\\label_map.pbtxt -o Tensorflow\\workspace\\annotations\\train.record
##python file_name -x Tensorflow\\workspace\\images\\test -l Tensorflow\\workspace\\annotations\\label_map.pbtxt -o Tensorflow\\workspace\\annotations\\test.record
#%%