from StdSuites.Standard_Suite import _3c_

__author__ = 'Hadoop'

import pandas;
import numpy;
import csv;
from collections import Counter;

def print_stat(f):
    print type(f)
    print len(f)


def describer(df):

    info = []

    # Gather Integer type columns statistics
    for i in range(2,15):
        df_temp = df[df.keys()[i]];
        df_temp = df_temp.dropna();
        col_name = "I"+str(i-1)
        info.append([col_name, df_temp.min(),df_temp.max(),df_temp.mean(), df_temp.std(), len(df)-len(df_temp), df_temp.quantile(q=0.25), df_temp.quantile(q=0.50),df_temp.quantile(q=0.75), df_temp.quantile(q=0.95)])
    # Gather Character type columns statistics
    for j in range(15,41):

        df_temp = df[df.keys()[j]];
        df_temp_no_nan = df_temp.dropna()
        col_name = "C"+str(j-14)
        c = Counter(df_temp_no_nan)

        # Following information are appended into info list: mode, percentage of the mode , number of non-nan values, number of distinct values
        l_mode = c.most_common(1)[0] # mode has list (element value, count)
        info.append([col_name, l_mode[0], round(float(l_mode[1])/float(len(df_temp)), 5) ,len(df_temp_no_nan), len(numpy.unique(df_temp_no_nan))])

    return info


def get_numeric_columns(df, filename):

    # x for x in range(2, 50) if x not in noprimes
    # df = df[k for k in df.keys() if k not  'C']
    df = df[[x for x in df.keys() if 'C' not in x]]
    print df.keys()
    i2_mean = 0.988349163
    i2_std  = 5.284200889
    i5_mean = 18533.61431
    i5_std  = 69310.21955
    i6_mean = 116.2114274
    i6_std  = 359.8823374
    df['I2'] = (df['I2'] - i2_mean)/i2_std
    df['I5'] = (df['I5'] - i5_mean)/i5_std
    df['I6'] = (df['I6'] - i6_mean)/i6_std
    f = '/Users/Hadoop/Documents/Kaggle/Display_Advertising_Challenge/train/int_only/' + filename
    df.to_csv(f, header=False, index=False)

def fill_missing_val(df, filename):

    # Drop I12 and C26 columns that are not necessary for this analysis
    df.drop(['I12'], axis=1, inplace=True)
    df.drop(['C26'], axis=1, inplace=True)

    # Missing I/C Column data value dictionary
    dict_missing_i_val = {'I1':1, 'I2':2.7944, 'I3':6.156, 'I4':4.158, 'I5':2814.81, 'I6':32.522, 'I7':3.1623, 'I8':7.249, 'I9':38.4632, 'I10':0.6181, 'I11':1, 'I13':4.199}
    dict_missing_c_val = {'C6':'7e0ccccf', 'C19':'21ddcdc9', 'C20':'b1252a9d', 'C22':'ad3062eb', 'C25':'001f3601'}


    for key in dict_missing_i_val.keys():
        df[key].fillna(dict_missing_i_val[key], inplace=True)

    for key in dict_missing_c_val.keys():
        df[key].fillna(dict_missing_c_val[key], inplace=True)

    df.dropna(inplace=True)

    f = '/Users/Hadoop/Documents/Kaggle/Display_Advertising_Challenge/train' + filename
    df.to_csv(f, header=False, index=False)




def outlier_describer(df):
    series_index = pandas.Series(range(0,100000))
    df['index'] = series_index

    I_Q95 = [15.11601732, 519.6316017,75.82781385,25.2017316, 63936.71266 ,474.9099567, 64.8965368, 41.59253247, 431.7724026, 2,10.47402597,3.629545455,28.84621212]
    dict_list_outlier_index = {}
    list_outlier_index_for_each_col = []

    for i in range(2,15):
        df_col = df[df[df.keys()[i]] >= I_Q95[i-2]]
        dict_list_outlier_index = {}
        for j in df_col['index']:
            dict_list_outlier_index.update({df['index'][j]: 1})
        list_outlier_index_for_each_col.append(dict_list_outlier_index)

    col_outlier_ratio = []
    # print len(list_outlier_index_for_each_col[4])
    # print list_outlier_index_for_each_col[4]

    for each_outlier_col_dict in list_outlier_index_for_each_col:
        counter = 0
        for k in each_outlier_col_dict.keys():
            if list_outlier_index_for_each_col[8].has_key(k):
                counter += 1
        # print "count", counter
        # print "length", len(each_outlier_col_dict)
        col_outlier_ratio.append(float(float(counter)/float(len(each_outlier_col_dict))))
    print col_outlier_ratio

def file_output(info, filename):
    col = ['stats']

    df_info = pandas.DataFrame(columns = col)
    with open('eggs.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for item in info:
            for i in item:
                # print i
                # df_info.append(i)
                csvwriter.writerow(i)

    print df_info
    df_info.to_csv('info.csv')

def file_output2(info, filename) :
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in info:
            csvwriter.writerow(i)
    csvfile.close()