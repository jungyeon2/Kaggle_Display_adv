import analysis_lib
import describer

__author__ = 'Hadoop'

import pandas;
import numpy;
import scipy;
import csv;
import matplotlib;
import matplotlib.pyplot as plt;
import statsmodels.api as sm;
import os;
from analysis_lib import *;
from pandas.core.frame import DataFrame;

file_loc = '/Users/Hadoop/Documents/Kaggle/Display Advertising Challenge/train'
# train_file = file_loc + 'train.csv'




#Run following shell script to split large train data into smaller subsets
#split -l 100000 file_loc/filename target_filename

#   read all training subsets
#   For each subset, get summary
header = pandas.DataFrame()
info = []
for subdir, dirs, files in os.walk(file_loc):
    for file in files:
        if file != '.DS_Store':
            if file.endswith('aa'):
                header = pandas.read_csv(file_loc+'/'+file, sep=',', nrows=1)
                f = pandas.read_csv(file_loc+'/'+file, sep=',', skiprows=1, header=None)
            else:
                f = pandas.read_csv(file_loc+'/'+file, sep=',')
            info.append(analysis_lib.describer(f))

analysis_lib.file_output(info, 'file_info.csv')



# t = pandas.read_csv(train_file, sep=',', nrows=100)
# t = t.dropna() #drops any NaN row
#
# print t.describe()
#      # Instead of running describe, we can use following code
#      # for i in range(len(numdata.columns)):
#      #        series = numdata.iloc[:, i]
#      #        destat.append([series.count(), series.mean(), series.std(),
#      #                       series.min(), series.quantile(lb), series.median(),
#      #                       series.quantile(ub), series.max()])
#
# col_names = t.keys()
#
# Y = t[t.keys()[1]]
# X = t[t.keys()[2:]]
#
# #pandas.factorize
# ## Encode input values as an enumerated type or categorical variable
# ## Factorize input: 1d array -> run factorize for each column
# print t[t.keys()[15:]].describe()
#
# M = numpy.ndarray(1)
# for i in t[t.keys()[15:]]:
#     if numpy.unique(pandas.factorize(t[i])[0])[-1] <= 1000:
#         t[i]= pandas.factorize(t[i])[0]
#     else:
#         t = t.drop(i,1)
#
#
# Y = t['Label']
# X = t[t.keys()[2:]]
# logistic_reg_model = sm.GLM(Y, X, family = sm.families.Binomial())
# linear_reg_model = sm.OLS(Y,X) #ols linear regression can detect multicollinearity
# logistic_result = logistic_reg_model.fit()
# linear_result = linear_reg_model.fit()
#
#
# print logistic_result.summary()