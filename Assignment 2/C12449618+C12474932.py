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
    
    
    
    trainingSet = numerify(trainingSet)
    queries = numerify(queries)
    print("Finished formatting")
    
    #Create new dataframes, place data inside them
    x_trainer = pd.DataFrame(index = trainingSet.index, columns = relevantFeatures)
    y_trainer = pd.DataFrame(index = trainingSet.index, columns = ['y'])
    
    x_queries = pd.DataFrame(index = queries.index, columns = relevantFeatures)
    
    for types in relevantFeatures:
        for x in range(0, len(trainingSet.index)):
            x_trainer.set_value(x, types, trainingSet.iloc[x][types])
            
        for x in range(0, len(queries.index)):
            x_queries.set_value(x, types, queries.iloc[x][types])
            
    for x in range (0, len(trainingSet.index)):
        y_trainer.set_value(x, 'y', trainingSet.iloc[x]['y'])
        
    
    ##Create the random forest model
    model = rfc(n_estimators=1000)


    #Fit the values into the model.
    y_train = y_trainer["y"].values
    model.fit(x_trainer, y_train)
    

    #
    #
    #DO MORE CODE HERE, QUERY OUR MODEL, RETRIEVE ANSWERS FOR QUERIES, APPEND IT TO answerData
    #
    #
    
    
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
    

    
#Methods to parse relevant data
def job_to_numeric(x):
    if x == 'unknown':
        return 0
    else:
        y = x[6:]
        return int(y)
        
#convert housing to numeric
def houseLoan_to_numeric(x):
    if x == 'yes':
        return 0
    if x == 'no':
        return 1
        
#convert loan to numeric
#see above
#convert contact to numeric
def contact_to_numeric(x):
    if x == 'unknown':
        return 0
    if x == 'telephone':
        return 1
    if x == 'cellular':
        return 2
    
def y_to_numeric(x):
    if x == 'TypeA':
        return 0
    if x == 'TypeB':
        return 1


def numerify(data):
    #made all data numeric
    length = len(data.index)
    print(length)
    
    for x in range (0, length):
        newjob = job_to_numeric(data.iloc[x]['job'])
        data.set_value(x, 'job', newjob)
        
        newhouse = houseLoan_to_numeric(data.iloc[x]['housing'])
        data.set_value(x, 'housing', newhouse)
        
        newloan = houseLoan_to_numeric(data.iloc[x]['loan'])
        data.set_value(x, 'loan', newloan)
        
        newcontact = contact_to_numeric(data.iloc[x]['contact'])
        data.set_value(x, 'contact', newcontact)
        
        if data.iloc[x]['y'] != '?':
            newy = y_to_numeric(data.iloc[x]['y'])
            data.set_value(x, 'y', newy)
        
    return data


if __name__ == '__main__':
    main()
    
