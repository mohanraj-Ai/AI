import pandas as pd
import numpy as np
class univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnname in dataset.columns:
            #print(columnname)
            if(dataset[columnname].dtype=='O'):
                #print("qual")
                qual.append(columnname)
            else:
                #print("quan")
                quan.append(columnname)
        return quan,qual   
    
    def freqtable(columnName,dataset):
        freqtable=pd.DataFrame(columns=["unique_values","Frequency","Relative Frequency","custom"])
        freqtable["unique_values"]=dataset[columnName].value_counts().index
        freqtable["Frequency"]=dataset[columnName].value_counts().values
        freqtable["Relative Frequency"]=(freqtable["Frequency"]/103)
        freqtable["custom"]=freqtable["Relative Frequency"].cumsum()
        return freqtable
    
    def univariate(dataset,quan):
        
        descriptive=pd.DataFrame(index=["mean","Median","Mode","Q1:25%","Q2:50%",
                               "Q3:75%","99","Q4:100","IQR","1.5rule","Lesser","Greater","Min","Max","kurtosis","skew","var","std"],columns=quan)
           
        for columnName in quan:
            descriptive[columnName]["mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5* descriptive[columnName]["IQR"]  
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
            descriptive[columnName]["var"]=dataset[columnName].var()
            descriptive[columnName]["std"]=dataset[columnName].std()
        return descriptive
        
    def lesserGreater(columnName):
        lesser=[]
        greater=[]
        for columnName in quan:
            if (descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
                lesser.append(columnName)
            if (descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]):
                greater.append(columnName)
        return lesser,greater
            
    def outlierfix(columnName):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
    
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
        return lesser,greater
