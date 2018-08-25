'''
Created on Apr 23, 2018

@author: rsepulveda3
'''

#import sys
#sys.path.append('C:\ProgramData\Anaconda3\Lib\site-packages')
import datetime



import matplotlib.pyplot as plt

from sklearn import tree
import graphviz 
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
import sklearn.datasets
import random
import numpy as np
import csv
from load_data import load_data1
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import itertools
from sklearn import svm
from sklearn import neighbors

#works
names=['bad0','bad1','bad2','bad3','middle4','good5','good6','good7','good8','good9'] #target names
info_w1=load_data1.loader("data/winequality-white.csv",names) #load info and bunch for training (data, target, feature names, target names)
info_r1=load_data1.loader("data/winequality-red.csv",names)

info_comb_data=[]
info_comb_targ=[]
for x in range(len(info_w1.data)):
    info_comb_data.append(info_w1.data[x])
    #info_comb_targ.append(info_w1.target[x])
    info_comb_targ.append(1) #1 = white wine
for x in range(len(info_r1.data)):
    info_comb_data.append(info_r1.data[x])
    #info_comb_targ.append(info_r1.target[x])
    info_comb_targ.append(2) #2 = red wine




info_wine=load_wine()


#info = load_iris()

#print(type(info[0]))

#Xtrain, Xtest, Ytrain, Ytest = train_test_split(info_comb_data, info_comb_targ, test_size=0.33)
Xtrain, Xtest, Ytrain, Ytest = train_test_split(info_w1.data, info_w1.target, test_size=0.33)

DTlf=tree.DecisionTreeClassifier(max_depth=10) #create decision classifier
BDTlf = RandomForestClassifier(n_estimators=10)
#SVMlf = svm.SVC(kernel='linear', C=1)
KNNlf=neighbors.KNeighborsClassifier(n_neighbors=1, metric='manhattan')

DTfit=DTlf.fit(Xtrain, Ytrain) #fit classifier
BDTfit = BDTlf.fit(Xtrain, Ytrain)
KNNfit=KNNlf.fit(Xtrain, Ytrain)


start = datetime.datetime.now()

#SVMfit=SVMlf.fit(Xtrain, Ytrain)

T_elap=datetime.datetime.now()-start




print("DT=" , DTfit.score(Xtest, Ytest))
print("BDT=" , BDTfit.score(Xtest, Ytest))
#print("svm=" , SVMlf.score(Xtest, Ytest))
print("KNN=" , KNNfit.score(Xtest, Ytest))
#print("time" , T_elap.seconds,":",T_elap.microseconds)


#table

arra=np.array(Xtrain).T
train_cov=np.cov(arra)
#print(train_cov)
row_label=info_w1.feature_names
col_label=info_w1.feature_names





fig, ax = plt.subplots()        
im = ax.imshow(train_cov)
print(im)


ax.set_xticks(np.arange(len(col_label)))
ax.set_yticks(np.arange(len(row_label)))
ax.set_xticklabels(col_label)
ax.set_yticklabels(row_label)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(col_label)):
    for j in range(len(row_label)):
        text = ax.text(j, i, '%0.1f' % train_cov[i, j],
                       ha="center", va="center", color="w")


plt.show()





'''
img = tree.export_graphviz(fits, out_file=None,  # create grafphiz image obbject and paramaters for visualization
                           feature_names=info_w1.feature_names,  
                           class_names=info_w1.target_names,  
                           filled=True, rounded=True,  
                           special_characters=True)

graph = graphviz.Source(img) #call image
graph.render("test",view=True) #print image

'''