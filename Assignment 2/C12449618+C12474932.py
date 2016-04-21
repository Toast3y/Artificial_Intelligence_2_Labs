# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:11:02 2016

@author: Christopher Jerrard-Dunne
@student_number: C12449618

@author2: Marcus Daly
@student_number2: C12474932
"""

import sys
import pandas as pd
import numpy as np
import csv
#import random
from sklearn.ensemble import RandomForestClassifier as rfc

def main():
    
    trainingSet_dir = ""
    queries_dir = ""
    
    features = ["ID","age","job","marital","education","default","balance","housing","loan","contact","day","month","duration","campaign","pdays","previous","poutcome","y"]
    dataHeader = ["ID","Y"]
    idnum = [0]
    target = [17]
    cont = [1, 5, 6, 10, 12, 13, 14, 15]
    cat = [2, 3, 4, 7, 8, 9, 11, 16]
    answerData = []
    
    #Find the datasets in the Data folder.
    if len(sys.argv) != 3:
        print("Usage: python filename [training_set] [queries]")
    else:
        trainingSet_dir = "./Data/" + sys.argv[1]
        queries_dir = "./Data/" + sys.argv[2]
        
    
    #Attempt to open the training and query datasets
    try:
        trainingSet = pd.read_csv(trainingSet_dir, header = None, names = features)
    except:
        print("ERROR: Cannot find data file " + trainingSet_dir + " in Data folder. Program will now close.")
        sys.exit()
        
    try:
        queries = pd.read_csv(queries_dir, header = None, names = features)
    except:
        print("ERROR: Cannot find data file " + queries_dir + " in Data folder. Program will now close.")
        sys.exit()
    
    
    
    
    
    ##Continuous Relevant Data: age, balance, previous
    ##Categorical Relevant Data: job, housing, loan, contact
    ##
    ##INSERT CODE THAT DOES THINGS HERE
    ##Implement Random Forest predictive algorithm
    ##Format data into numerical format
    
    relevantFeatures = ["age","balance","previous","job","housing","loan","contact"]
    
    model = rfc(n_estimators=1000)
    x_trainer = trainingSet[relevantFeatures].values 
    y_trainer = trainingSet["y"].values
    
    
    
    #convert 
    
    model.fit(x_trainer, y_trainer)
    
    
    
    #Format the data and put it into a list to write to file.
    answerData.append(dataHeader)
    length = len(trainingSet.index)

    for x in range (0, length):
        temp = []
        newid = trainingSet.iloc[x]['ID']
        temp.append(newid)
        newtarget = trainingSet.iloc[x]['y']
        temp.append(newtarget)
        answerData.append(temp)
    
    #Write all the data from the array into a text file.
    #Each iteration of queries should be written into the answerData list, as lists themselves.
    newfile = open('./data/C12449618+C12474932.txt', 'w')
    writerObject = csv.writer(newfile, lineterminator='\n')
    
    for line in answerData:
        writerObject.writerow(line)
        
    newfile.flush()
    newfile.close()
    

if __name__ == '__main__':
    main()