# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:45:54 2016

@author: Toast3y
"""

import pandas as pd
import matplotlib as mpl
from collections import Counter
import numpy as np
import csv
import sys



contDataHeader = ["Feature", "Count", "% Miss.", "Card.", "Min.", "1st Qrt.", 
                  "Mean", "Median", "3rd Qrt.", "Max.", "Std. Dev."]
cateDataHeader = ["Feature", "Count", "% Miss.", "Card.", "Mode", "Mode Freq.",
                  "Mode %", "2nd Mode", "2nd Mode Freq.", "2nd Mode %"]


#Open files for data entry
try:
    featureset = open('./data/featurenames.txt', 'r')
except:
    print("ERROR: Expected file not found. Program will now terminate.")
    sys.exit()

#Format features into a list for easy use
features = featureset.read().splitlines()

#Remove any empty features from the featureset list
for feature in features:
    if feature == "":
        features.remove(feature)
        


#Open and create the table and format it properly within the dataframe
try:
    dataset = pd.read_csv("./data/Dataset.txt", header=None, names=features)
except:
    print("ERROR: Expected file not found. Program will now terminate.")
    sys.exit()




#Filter the datatypes based on what Pandas views it as
contDataFeature = []
cateDataFeature = []

for feature in features:
    if(dataset[feature].dtypes == "int64"):
        contDataFeature.append(feature)
    elif (dataset[feature].dtypes == "object"):
        cateDataFeature.append(feature)
        

#Create Data arrays to write into the files, append the header
contData = []
cateData = []
contData.append(contDataHeader)
cateData.append(cateDataHeader)



#Create analytical data for each feature within the dataset

#Continuous data
for feature in contDataFeature:
    #Create a temporary storage array. Each row in the data is kept as a comma
    #Separated list. This is done to ensure the correct writing of the csv file
    tempContData = []
    
    #Attach the feature name
    tempContData.append(feature)
    
    #Count all entries for the feature in the list
    tempContData.append(len(dataset[feature]))
    
    #Count the number of missing fields in the data
    percentMissing = np.count_nonzero(dataset[feature].isnull()/len(dataset[feature])*100)
    tempContData.append(percentMissing)
    
    #Get the cardinality
    tempContData.append(len(dataset[feature].unique()))
    
    #Find the minimum
    tempContData.append(dataset[feature].min())
    
    #First Quartile
    tempContData.append(dataset[feature].quantile(0.25))
    
    #The average / mean
    tempContData.append(round(dataset[feature].mean(), 4))
    
    #The median
    tempContData.append(dataset[feature].median())
    
    #3rd Quartile
    tempContData.append(dataset[feature].quantile(0.75))
    
    #Maximum
    tempContData.append(dataset[feature].max())
    
    #Standard Deviation
    tempContData.append(round(dataset[feature].std(),4))
    
    
    #Append all data to the list
    contData.append(tempContData)
    
    

#print(contData)
#Categorical data
for feature in cateDataFeature:
    #Create a temporary storage array. Each row in the data is kept as a comma
    #Separated list. This is done to ensure the correct writing of the csv file
    tempCateData = []
    
    #Attach the feature name
    tempCateData.append(feature)
    
    #Count all entries for the feature in the list
    tempCateData.append(len(dataset[feature]))
    
    #Count the number of missing fields in the data
    percentMissing = np.count_nonzero(dataset[feature].isnull()/len(dataset[feature])*100)
    tempCateData.append(percentMissing)
    
    #Cardinality
    tempCateData.append(len(dataset[feature].unique()))
    
    #Mode
    tempCateData.append(Counter(dataset[feature]).most_common(1)[0][0])
    
    #Mode Frequency
    tempCateData.append(Counter(dataset[feature]).most_common(1)[0][1])
    
    #Mode %
    tempCateData.append((Counter(dataset[feature]).most_common(1)[0][1]/len(dataset[feature]))*100)
    
    #2nd Mode
    tempCateData.append(Counter(dataset[feature]).most_common(2)[-1][0])
    
    #2nd Mode Frequency
    tempCateData.append(Counter(dataset[feature]).most_common(2)[-1][1])
    
    #2nd Mode %
    tempCateData.append((Counter(dataset[feature]).most_common(2)[-1][1]/len(dataset[feature]))*100)
    
    
    #Append all data to the list
    cateData.append(tempCateData)



#Create the files and output them into the correct folder
#Continuous Data File
try:
    newfile = open('./data/C12449618CONT.csv', 'w')
    writerObject = csv.writer(newfile, lineterminator='\n')
    
    #Write each line into the new file
    for line in contData:
        writerObject.writerow(line)
except:
    print('ERROR: Unable to write C12449618CONT.csv file.')

    
#Categorical Data File
try:
    newfile2 = open('./data/C12449618CATE.csv', 'w')
    writerObject2 = csv.writer(newfile2, lineterminator='\n')
    
    #Write each line into the new file
    for line in cateData:
        writerObject2.writerow(line)
except:
    print('ERROR: Unable to write C12449618CONT.csv file.')
