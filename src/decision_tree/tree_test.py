'''
Created on Apr 23, 2018

@author: rsepulveda3
'''


from sklearn import tree
import graphviz 
from sklearn.datasets import load_iris
import sklearn.datasets
import random
import numpy as np
import csv
from load_data import load_data1

decsicion=tree.DecisionTreeClassifier()

iris = load_iris()
#print(iris)

with open("data/winequality-white.csv") as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = [r for r in reader]
    #next(reader) # skip header
    
    
feature=data[0] #copies first row of CVS (header) to feature
data.pop(0) #removes firsst row - leaving only data)
data1=[list(map(float, data[r])) for r in range(len(data))]  # conversts strings to float values
target1=[data1[i][-1] for i in range(len(data1))]
datas=[data1[i][0:-1] for i in range(len(data1))]
#print("data ", data)

data2=sklearn.datasets.base.Bunch(data= datas,target= target1,feature_names=feature)
'''
target=range(9)
data2=sklearn.datasets.base.Bunch(data= datas,target= target1,feature_names=feature, target_names=target)
'''
#print(data2)

decsicion=tree.DecisionTreeClassifier()
decsicion= decsicion.fit(data2.data, data2.target)

t_p=[[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
#t_p.reshape(-1, 1)
pred=decsicion.predict(t_p)
print(pred)

dot_data = tree.export_graphviz(decsicion, out_file=None) 
'''
dot_data = tree.export_graphviz(decsicion, out_file=None, 
                                        feature_names=data2.feature_names,  
                                        #class_names=data2.target_names,  
                                        filled=True, rounded=True,  
                                        special_characters=True) 








graph = graphviz.Source(dot_data) 
graph.render("test",view=True)
#graph.render("test")
'''

'''
#works
info=load_data1.loader("data/winequality-white.csv")
print(info)

'''

    

