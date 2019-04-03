# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 15:00:21 2018

@author: Saloni Gupta
"""

#libraries
import pandas as pd
import math

#dataset - iris

#loading dataset
data = pd.read_csv("breast_cancer.txt")

data.columns = ["Sample code number","Clump Thickness" ,"Uniformity of Cell Size","Uniformity of Cell Shape","Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli","Mitoses","Class"]

data = data.astype('float64')




#preprocessing of the dataset

#finding number of attribute in dataset
list_attr = data.columns.values
print list_attr

l = list_attr[-1]
classes = data[l].unique()
#print l
#print classes
df = data.groupby(l)

#print df.describe().head()

train_dataset = pd.DataFrame(columns = list_attr)

test_dataset = pd.DataFrame(columns = list_attr)

#print train_dataset

for i in classes:
    df = data[data[l] == i]
    count_row = df.shape[0]
    #print count_row
    test_size = int(math.ceil((count_row*1)/5))
    #print test_size
    train_size = int((count_row*4)/5)
    #print train_size
    #print df[:train_size]
    train_dataset = train_dataset.append(df[ : train_size])
    #train_dataset = train_dataset.reset_index()
    #print train_dataset
    test_dataset = test_dataset.append(df[train_size : ])
    
print train_dataset.head()
print train_dataset.shape
print test_dataset.shape
#print train_dataset.head()
#print test_dataset.head() 
#print train_data
#print data.tail()

k = 5
#print train_data.head()

test_dataset["Predicted_class"] = ""
train_dataset["distance"] =  ""
#print data.tail()
for i in range(0,test_dataset.shape[0]):
    sum = 0
    for j in range(0,train_dataset.shape[0]):
        for k in range(1,len(list_attr)-1):
            sum = sum + pow((train_dataset.iloc[j,k]-test_dataset.iloc[i,k]),2)
        res = math.sqrt(sum)
        train_dataset.loc[j,'distance'] = res
.        
    sorted_data = train_dataset.sort_values('distance')
    #print sorted_data.head()
    #print sorted_data
    label = []
    
    for m in range(0,k):
        label.append(sorted_data.iloc[m,5])
    
    l = max(label,key=label.count)
    
    #print l
    
    test_dataset.loc[i,'Predicted_class'] = l


#print test_dataset.head()    
c = 0
for i in range(0,30):
    if test_dataset.iloc[i,len(list_attr)-1] != test_dataset.iloc[i,len(list_attr)]:
        c = c + 1
#print c
        
sample = test_dataset.shape[0]
print "Accuracy % " , ((sample-c)*100)/sample
        

