__author__ = 'Hadoop'

#this file will do data massaging on testing set
import pandas;
import numpy;
import scipy;
import csv;
import matplotlib;
import matplotlib.pyplot as plt;
import statsmodels.api as sm;


file_loc = '/Users/Hadoop/Documents/Kaggle/Display Advertising Challenge/test/'
test_file = file_loc + 'test_short.csv'

f = pandas.read_csv(test_file, sep=',');

#