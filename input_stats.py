from pandas.core.frame import DataFrame

__author__ = 'Hadoop'

import pandas;
import numpy;
import scipy;
import csv;
import matplotlib;
import matplotlib.pyplot as plt;
import statsmodels.api as sm;

from analysis_lib import *;

file_loc = '/Users/Hadoop/Documents/Kaggle/Display Advertising Challenge/train/'
train_file = file_loc + 'train.csv'


t = pandas.read_csv(train_file, sep=',', nrows=500000)
t = t.dropna() #drops any NaN row
#print t[t.keys()[0]]
#print t['I1'].describe()

print t.describe()
col_names = t.keys()
#for k in t.keys():
   # print t[k].describe()
   # print ''
#plt.plot(t['I2'] )
#plt.show()
Y = t[t.keys()[1]]
X = t[t.keys()[2:]]
#print Y
#print type(t['C3'])

#pandas.factorize
## Encode input values as an enumerated type or categorical variable
## Factorize input: 1d array -> run factorize for each column
print t[t.keys()[15:]].describe()

M = numpy.ndarray(1)
for i in t[t.keys()[15:]]:
    #M = numpy.append(M, pandas.factorize(t[i])[0])
    #print pandas.factorize(t[i])[0]
    if numpy.unique(pandas.factorize(t[i])[0])[-1] <= 1000:
        t[i]= pandas.factorize(t[i])[0]
    else:
        t = t.drop(i,1)

    #print numpy.unique(pandas.factorize(t[i])[0])
    #if numpy.unique(pandas.factorize(t[i])[0])[-1] <= 1000:
    #    M.append(pandas.factorize(t[i])[0])

#print t

#M = [x for x in t if <= 1000]
#print M

#M = [x for x in S if x % 2 == 0]
# M = pandas.core.frame.DataFrame()
# for i in t[t.keys()[15:]]:
#     print i
#     csv.writer()
#     M.append([x for x in t[i] if numpy.unique(x) <= 1000])
# print M
#print M
#M = []


Y = t['Label']
X = t[t.keys()[2:]]
logistic_reg_model = sm.GLM(Y, X, family = sm.families.Binomial())
linear_reg_model = sm.OLS(Y,X) #ols linear regression can detect multicollinearity
logistic_result = logistic_reg_model.fit()
linear_result = linear_reg_model.fit()


print linear_result.summary()

from pandas.core.frame import DataFrame

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

file_loc = '/Users/Hadoop/Documents/Kaggle/Display Advertising Challenge/train/sub'
train_file = file_loc + 'train.csv'

#Run following shell script to split large train data into smaller subsets
#split -l 100000 file_loc/filename target_filename

#   read all training subsets
#   For each subset, get summary
for subdir, dirs, files in os.walk(file_loc):
    for file in files:
        f = pandas.read_csv(file, sep=',')
        print f.describe()

#
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         f=open(rootdir+file,'r') #use the absolute URL of the file
#         lines = f.readlines()
#         f.close()
#         f=open(file,'w') #universal mode can only be used with 'r' mode
#         for line in lines:
#             newline=doWhatYouWant(line)
#             f.write(newline)
#         f.close()


t = pandas.read_csv(train_file, sep=',', nrows=100)
t = t.dropna() #drops any NaN row

print t.describe()
     # Instead of running describe, we can use following code
     # for i in range(len(numdata.columns)):
     #        series = numdata.iloc[:, i]
     #        destat.append([series.count(), series.mean(), series.std(),
     #                       series.min(), series.quantile(lb), series.median(),
     #                       series.quantile(ub), series.max()])

col_names = t.keys()

Y = t[t.keys()[1]]
X = t[t.keys()[2:]]

#pandas.factorize
## Encode input values as an enumerated type or categorical variable
## Factorize input: 1d array -> run factorize for each column
print t[t.keys()[15:]].describe()

M = numpy.ndarray(1)
for i in t[t.keys()[15:]]:
    if numpy.unique(pandas.factorize(t[i])[0])[-1] <= 1000:
        t[i]= pandas.factorize(t[i])[0]
    else:
        t = t.drop(i,1)


Y = t['Label']
X = t[t.keys()[2:]]
logistic_reg_model = sm.GLM(Y, X, family = sm.families.Binomial())
linear_reg_model = sm.OLS(Y,X) #ols linear regression can detect multicollinearity
logistic_result = logistic_reg_model.fit()
linear_result = linear_reg_model.fit()


print logistic_result.summary()

import oauth2;

api_key             = "RmtiJc07cMrSYoFUwbokQtcY9"
api_secret          = "ZkdQ25btgmZATQFwuQKy5OHicTHSexaUC3jPfEvOnmu6pNdjnf"
access_token_key    = "176684082-DnVnvjYT9yfi6C2hR9A7FMmNnvrrmaBHjZJ2GzWM"
access_token_secret = "aROC74IYAtC2cvmZlQy46CXsyYjUzgavNWe43Pv0Wbkd4"
