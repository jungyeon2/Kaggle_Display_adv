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

# train_file = file_loc + 'train.csv'

#Run following shell script to split large train data into smaller subsets
#split -l 100000 file_loc/filename target_filename

#   read all training subsets
#   For each subset, get summary
def main():
    file_loc = '/Users/Hadoop/Documents/Kaggle/Display_Advertising_Challenge/train'
    header = pandas.DataFrame()
    info = []

    for subdir, dirs, files in os.walk(file_loc):
        for file in files:
            print file
            if file != '.DS_Store' and file != '.testinput.swp':
                if file.endswith('aa'):
                    df_header = pandas.read_csv(file_loc+'/'+file, sep=',', nrows=1)
                    orignal_header = ['Id','Label','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']
                    header = ['Id','Label','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25']
                    # f = pandas.read_csv(file_loc+'/'+file, sep=',', skiprows=1, header=None)
                    f = pandas.read_csv(file_loc+'/'+file, sep=',', skiprows=1, header=None, names=header)
                else:
                    # f = pandas.read_csv(file_loc+'/'+file, sep=',', header=None)
                    f = pandas.read_csv(file_loc+'/'+file, sep=',', header=None, names=header)
                # info.append(analysis_lib.describer(f))
                # f.set_header(header, inplace=True)
                # print f
                # analysis_lib.fill_missing_val(f, file)
                analysis_lib.get_numeric_columns(f,file)
                # info.append(analysis_lib.outlier_describer(f))
    # analysis_lib.file_output(info, 'file_info.csv')



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

if __name__ == '__main__':
    main()