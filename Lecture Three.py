# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:21:07 2017

@author: sarahwright
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# load data, specify sheet and number of rows to skip
df_data = pd.read_excel('HenryHub.xls',sheetname ='Data 1',skiprows = [0,1])

# renaming the very long price column name
df_data.columns = ['date','price']

def annual_profile(df_data):
    
    #number of years in record
    num_years = int(len(df_data)/12)
    
    #output matrix of zeros
    output = np.zeros((12,num_years))
    
    #nested for loops
    for i in range(0,num_years):
        for j in range(0,12):
            output[j,i] = df_data.loc[i*12+j,'price']
    
    #years considered    
    years = range(1997,2017)
    
    #index of 2008
    a = years.index(2008)
    
    #select data from 2008-present
    m = output[:,a:]
    
    return m

#call annual profile function
x = annual_profile(df_data)

def monthly_stats(stuff):
    output = np.zeros((12,2))
    for j in range(0,12):
        output[j,0] = np.average(stuff[j,:])
        output[j,1] = np.std(stuff[j,:])
    return output


y = monthly_stats(x)


a = np.random.normal(y[0,0],y[0,1],1000)
b = np.random.normal(y[3,0],y[3,1],1000)
plt.figure() #synthetic
plt.hist(b)
plt.hist(a)
plt.figure() #HH data
plt.hist(x[3,:])
plt.hist(x[0,:])

