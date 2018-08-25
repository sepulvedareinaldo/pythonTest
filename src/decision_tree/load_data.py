


class load_data1:

    def loader(file, *args): #args is target names
        
        import sklearn.datasets
        import csv
        list(args)
        names=[]
        
        for x in range(len(args[0])):
            names.append(args[0][x])
            
        with open(file) as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            data = [r for r in reader]
        
        features=data[0] #copies first row of CVS (header) to feature
        features.pop(-1) #removes target column
        data.pop(0)#removes first row - leaving only data)
        data=[list(map(float, data[r])) for r in range(len(data))]# conversts strings to float values
        
        targets=[data[i][-1] for i in range(len(data))] #selects only targets - last row
        
        datas=[data[i][0:-1] for i in range(len(data))] #selects only data - without last row
        
        
        
     
        if len(args)>0: #checks to see if we input target names - args is target names
            answer= sklearn.datasets.base.Bunch(data=datas, 
                                                 target=targets, 
                                                 feature_names=features,
                                                 target_names=names
                                                 )
        else:
            answer=sklearn.datasets.base.Bunch(data=datas, 
                                    target=targets, 
                                    feature_names=features
                                    )

        
        return answer
    