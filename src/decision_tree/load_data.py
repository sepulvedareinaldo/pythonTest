


class load_data1:

    def loader(file):
        
        import sklearn.datasets
        import csv
        
        with open(file) as f:
            reader = csv.reader(f, delimiter=';', quotechar='"')
            data = [r for r in reader]
        
        features=data[0] #copies first row of CVS (header) to feature
        data.pop(0)#removes first row - leaving only data)
        data=[list(map(float, data[r])) for r in range(len(data))]# conversts strings to float values
        
        targets=[data[i][-1] for i in range(len(data))] #selects only targets - last row
        
        datas=[data[i][0:-1] for i in range(len(data))] #selects only data - without last row
        return sklearn.datasets.base.Bunch(data=datas, target=targets, feature_names=features)
    