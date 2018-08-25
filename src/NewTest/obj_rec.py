'''
Created on Jun 13, 2018

@author: rsepulveda3
'''
'''
# construct the argument parse and parse the arguments
 Users\rsepulveda3\workspace\pythonTest\model_obj

 --image add path to image
 Users\rsepulveda3\workspace\pythonTest\model_obj
 
 --prototxt path to Caffe 'deploy' prototxt file
 Users\rsepulveda3\workspace\pythonTest\model_obj\MobileNetSSD_deploy.prototxt.txt

 --model path to Caffe pre-trained model
 Users\rsepulveda3\workspace\pythonTest\model_obj\MobileNetSSD_deploy.caffemodel
 
 conf_default = 0.2

'''

import numpy as np
import argparse
import cv2

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
CONF_DEFAULT = 0.2

# load our serialized model from disk
print("[INFO] loading model...")

prototxt='C:/Users/rsepulveda3/workspace/pythonTest/model_obj/MobileNetSSD_deploy.prototxt'
model='C:/Users/rsepulveda3/workspace/pythonTest/model_obj/MobileNetSSD_deploy.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt, model)

image = cv2.imread('Piedmont.jpg')
(h, w) = image.shape[:2]

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,
                             (300, 300), 127.5)

print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

confidence=[]
for i in np.arange(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated with the
    # prediction
    confidence.append(detections[0, 0, i, 2])
 
    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence[i] > CONF_DEFAULT:
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
                # display the prediction
        
        label = '{}: {:.2f}%'.format(CLASSES[idx], confidence[i] * 100)
        #label= str(CLASSES[idx],' ',confidence[i] * 100)
        print("[INFO] {}".format(label))
        cv2.rectangle(image, (startX, startY), (endX, endY),
            COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
# show the output image

box_img=cv2.resize(image,(800,1000))

cv2.imshow("Output", box_img)
cv2.waitKey(0)
cv2.imshow("Output", image[:,:])
cv2.waitKey(0)
print('')
