'''
Created on May 22, 2018

@author: rsepulveda3
'''



#import sys
#sys.path.append('c:/Users/rsepulveda3/AppData/Local/Programs/Python/Python36-32/Lib/site-packages')

import numpy as np
import argparse
import time
import cv2


'''
asdf

 Users\rsepulveda3\workspace\pythonTest\model

 --image add path to image
 Users\rsepulveda3\workspace\pythonTest\model

 --prototxt path to Caffe 'deploy' prototxt file
 Users\rsepulveda3\workspace\pythonTest\model\bvlc_googlenet.prototxt

 --model path to Caffe pre-trained model
 Users\rsepulveda3\workspace\pythonTest\model\bvlc_googlenet.caffemodel

 --labels path to ImageNet labels (i.e., syn-sets)
 Users\rsepulveda3\workspace\pythonTest\model

asdf
'''



image = cv2.imread('dogo.jpg')
#blop= cv2.resize(image,(224,224))
blob = cv2.dnn.blobFromImage(image, 1, (224, 224),(104, 117, 123))
'''

image = cv2.imread('spain.jpg')
image2 = cv2.resize(image,(500,600))
blop = image2[50:300,100:400]
blop = cv2.resize(blop,(224, 224))
blob = cv2.dnn.blobFromImage(blop, 1, (224, 224),(104, 117, 123))
'''
rows = open('synset_words.txt').read().strip().split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

'''
img=cv2.imread('Piedmont.jpg')
'''
cv2.imshow('image',image)
#cv2.imshow('image',blop)
cv2.waitKey(0)
cv2.destroyAllWindows()


model='C:/Users/rsepulveda3/workspace/pythonTest/model/bvlc_googlenet.caffemodel'
prototxt='C:/Users/rsepulveda3/workspace/pythonTest/model/bvlc_googlenet.prototxt'
net = cv2.dnn.readNetFromCaffe(prototxt, model)

net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("[INFO] classification took {:.5} seconds".format(end - start))

idxsTest = np.argsort(preds[0])
idxs = np.argsort(preds[0])[::-1][:5]

#what=preds[0, 0, 1, 2]

for (i, idx) in enumerate(idxs):
    # draw the top prediction on the input image
    if i == 0:
        text = "Label: {}, {:.2f}%".format(classes[idx],
            preds[0][idx] * 100)
        cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 0, 255), 2)
 
    # display the predicted label + associated probability to the
    # console    
    print("[INFO] {}. label: {}, probability: {:.5}".format(i + 1,
        classes[idx], preds[0][idx]))

print(idxs)
print(preds[0,idxs[0]])

