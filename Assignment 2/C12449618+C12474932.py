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

def main():
    
    trainingSet_dir = ""
    queries_dir = ""
    idnum = [0]
    target = [17]
    cont = [1, 5, 6, 10, 12, 13, 14, 15]
    cat = [2, 3, 4, 7, 8, 9, 11, 16]
    
    #Find the datasets in the Data folder.
    if len(sys.argv) != 3:
        print("Usage: python filename [training_set] [queries]")
    else:
        trainingSet_dir = "./data/" + sys.argv[1]
        queries_dir = "./data/" + sys.argv[2]
        
    
    #Attempt to open the training and query datasets
    try:
        trainingSet = pd.read_csv(trainingSet_dir)
    except:
        print("ERROR: Cannot find data file " + trainingSet_dir + " in Data folder. Program will now close.")
        sys.exit()
        
    try:
        queries = pd.read_csv(queries_dir)
    except:
        print("ERROR: Cannot find data file " + queries_dir + " in Data folder. Program will now close.")
        sys.exit()
    
    

if __name__ == '__main__':
    main()