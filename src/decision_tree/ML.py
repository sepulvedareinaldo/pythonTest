'''
Created on Mar 3, 2018

@author: rsepulveda3
'''

class newMod:

    def __init__(self, spr):
        
        spread=spr
        
        from sklearn import tree
        import graphviz 
        from sklearn.datasets import load_iris
        import random
        import numpy as np
        
        
        
        iris = load_iris()
        #print (iris)
        decsicion=tree.DecisionTreeClassifier()
        
        decsicion= decsicion.fit(iris.data, iris.target)
        print (decsicion)
        
        
        
        
        n_nodes = decsicion.tree_.node_count
        children_left = decsicion.tree_.children_left
        children_right = decsicion.tree_.children_right
        feature = decsicion.tree_.feature
        threshold = decsicion.tree_.threshold
        
        
        #print('n_nodes : ', n_nodes)
        #print('children_left : ', children_left)
        #print('children_right : ', children_right)
        #print('feature : ', feature)
        #print('threshold : ', threshold)
        
        spread=0.5
        
        a=iris.data
        ran=random.sample(range(len(a)), round(spread*150))
        ran.sort()
        train=a[ran]
        valid=np.zeros((round((1-spread)*150),4))
        index=np.zeros((round((1-spread)*150)))
        temp1=0
        temp2=0
        n=0
        for i in np.isin(range(150),ran):
            
            if (i):
                #train[temp1]=a[n]
                temp1+=1
            else:
                valid[temp2]=a[n]
                index[temp2]=n
                temp2+=1
            
            n+=1
        
        #print(valid.shape, train.shape)
        
        #print (len(ran))
        '''
        print (ran[10])
        print (a[ran[10]])
        print (set[10])
        print(a.shape)
        '''
        estimator=tree.DecisionTreeClassifier()
        estimator= estimator.fit(iris.data[ran], iris.target[ran])
        
        
        
        pred=estimator.predict(valid)
        expec=iris.target[index.astype(int)]
        comps=np.zeros(pred.shape)
        #print(pred,expec)
        
        
        for i in range(len(pred)):
            if pred[i]==expec[i]:
                comps[i]=1
            else:
                comps[i]=0
        
        
        perc=comps.sum()/len(comps)
        #/len(comps).astype(int)
        print(perc)
        
        
        dot_data = tree.export_graphviz(decsicion, out_file=None, 
                                        feature_names=iris.feature_names,  
                                        class_names=iris.target_names,  
                                        filled=True, rounded=True,  
                                        special_characters=True) 
                                        
        graph = graphviz.Source(dot_data) 
        
         
        graph.render("test",view=True)
        graph.render("test")
        
        
        '''
        dot_data = tree.export_graphviz(decsicion, out_file=None) 
        graph = graphviz.Source(dot_data) 
        graph.render("test",view=True)
        graph.render("test")
        
        #graph.save('example1_graph.dot')
        '''
       
        
