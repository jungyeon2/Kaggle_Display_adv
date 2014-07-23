__author__ = 'Hadoop'

import pandas;
import numpy;
import csv;
from collections import Counter;

def print_stat(f):
    print type(f)
    print len(f)

def describer(df):
    col = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','I14','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25','C26']
    columns = ['I1_min', 'I1_max', 'I1_mean', 'I1_std', 'I1_num_nan', 'I1_Q25', 'I1_Q50', 'I1_Q75', 'I1_Q95',
               'I2_min', 'I2_max', 'I2_mean', 'I2_std', 'I2_num_nan', 'I2_Q25', 'I2_Q50', 'I2_Q75', 'I2_Q95',
               'I3_min', 'I3_max', 'I3_mean', 'I3_std', 'I3_num_nan', 'I3_Q25', 'I3_Q50', 'I3_Q75', 'I3_Q95',
               'I4_min', 'I4_max', 'I4_mean', 'I4_std', 'I4_num_nan', 'I4_Q25', 'I4_Q50', 'I4_Q75', 'I4_Q95',
               'I5_min', 'I5_max', 'I5_mean', 'I5_std', 'I5_num_nan', 'I5_Q25', 'I5_Q50', 'I5_Q75', 'I5_Q95',
               'I6_min', 'I6_max', 'I6_mean', 'I6_std', 'I6_num_nan', 'I6_Q25', 'I6_Q50', 'I6_Q75', 'I6_Q95',
               'I7_min', 'I7_max', 'I7_mean', 'I7_std', 'I7_num_nan', 'I7_Q25', 'I7_Q50', 'I7_Q75', 'I7_Q95',
               'I8_min', 'I8_max', 'I8_mean', 'I8_std', 'I8_num_nan', 'I8_Q25', 'I8_Q50', 'I8_Q75', 'I8_Q95',
               'I9_min', 'I9_max', 'I9_mean', 'I9_std', 'I9_num_nan', 'I9_Q25', 'I9_Q50', 'I9_Q75', 'I9_Q95',
               'I10_min', 'I10_max', 'I10_mean', 'I10_std', 'I10_num_nan', 'I10_Q25', 'I10_Q50', 'I10_Q75', 'I10_Q95',
               'I11_min', 'I11_max', 'I11_mean', 'I11_std', 'I11_num_nan', 'I11_Q25', 'I11_Q50', 'I11_Q75', 'I11_Q95',
               'I12_min', 'I12_max', 'I12_mean', 'I12_std', 'I12_num_nan', 'I12_Q25', 'I12_Q50', 'I12_Q75', 'I12_Q95',
               'I13_min', 'I13_max', 'I13_mean', 'I13_std', 'I13_num_nan', 'I13_Q25', 'I13_Q50', 'I13_Q75', 'I13_Q95',
               'I14_min', 'I14_max', 'I14_mean', 'I14_std', 'I14_num_nan', 'I14_Q25', 'I14_Q50', 'I14_Q75', 'I14_Q95',
               'C1_mode', 'C1_mode_ratio', 'C1_finite_count', 'C1_unique',
               'C1_mode', 'C1_mode_ratio', 'C1_finite_count', 'C1_unique',
               'C2_mode', 'C2_mode_ratio', 'C2_finite_count', 'C2_unique',
               'C3_mode', 'C3_mode_ratio', 'C3_finite_count', 'C3_unique',
               'C4_mode', 'C4_mode_ratio', 'C4_finite_count', 'C4_unique',
               'C5_mode', 'C5_mode_ratio', 'C5_finite_count', 'C5_unique',
               'C6_mode', 'C6_mode_ratio', 'C6_finite_count', 'C6_unique',
               'C7_mode', 'C7_mode_ratio', 'C7_finite_count', 'C7_unique',
               'C8_mode', 'C8_mode_ratio', 'C8_finite_count', 'C8_unique',
               'C9_mode', 'C9_mode_ratio', 'C9_finite_count', 'C9_unique',
               'C10_mode', 'C10_mode_ratio', 'C10_finite_count', 'C10_unique',
               'C11_mode', 'C11_mode_ratio', 'C11_finite_count', 'C11_unique',
               'C12_mode', 'C12_mode_ratio', 'C12_finite_count', 'C12_unique',
               'C13_mode', 'C13_mode_ratio', 'C13_finite_count', 'C13_unique',
               'C14_mode', 'C14_mode_ratio', 'C14_finite_count', 'C14_unique',
               'C15_mode', 'C15_mode_ratio', 'C15_finite_count', 'C15_unique',
               'C16_mode', 'C16_mode_ratio', 'C16_finite_count', 'C16_unique',
               'C17_mode', 'C17_mode_ratio', 'C17_finite_count', 'C17_unique',
               'C18_mode', 'C18_mode_ratio', 'C18_finite_count', 'C18_unique',
               'C19_mode', 'C19_mode_ratio', 'C19_finite_count', 'C19_unique',
               'C20_mode', 'C20_mode_ratio', 'C20_finite_count', 'C20_unique',
               'C21_mode', 'C21_mode_ratio', 'C21_finite_count', 'C21_unique',
               'C22_mode', 'C22_mode_ratio', 'C22_finite_count', 'C22_unique',
               'C23_mode', 'C23_mode_ratio', 'C23_finite_count', 'C23_unique',
               'C24_mode', 'C24_mode_ratio', 'C24_finite_count', 'C24_unique',
               'C25_mode', 'C25_mode_ratio', 'C25_finite_count', 'C25_unique',
               'C26_mode', 'C26_mode_ratio', 'C26_finite_count', 'C26_unique'
               ]
    # rtn_df = pandas.DataFrame(columns=columns)
    #rtn_df.fillna(0)
    # foo = pandas.DataFrame(columns=columns)
    info = []

    # Gather Integer type columns statistics
    for i in range(2,15):
        df_temp = df[df.keys()[i]];
        df_temp = df_temp.dropna();
        col_name = "I"+str(i-1)
        info.append([col_name, df_temp.min(),df_temp.max(),df_temp.mean(), df_temp.std(), len(df)-len(df_temp), df_temp.quantile(q=0.25), df_temp.quantile(q=0.50),df_temp.quantile(q=0.75), df_temp.quantile(q=0.95)])
        # info.append(df_temp.min(),df_temp.max(),df_temp.mean(), df_temp.std(), len(df)-len(df_temp), df_temp.quantile(q=0.25), df_temp.quantile(q=0.50),df_temp.quantile(q=0.75), df_temp.quantile(q=0.95))
    # Gather Character type columns statistics
    for j in range(15,41):
        df_temp = df[df.keys()[j]];
        df_temp_no_nan = df_temp.dropna()
        col_name = "C"+str(j-1)
        c = Counter(df_temp_no_nan)

        # Following information are appended into info list: mode, percentage of the mode , number of non-nan values, number of distinct values

        l_mode = c.most_common(1)[0] # mode has list (element value, count)
        info.append([col_name, l_mode[0], round(float(l_mode[1])/float(len(df_temp)), 5) ,len(df_temp_no_nan), len(numpy.unique(df_temp_no_nan))])

    return info
    # rtn_df.append(foo)

    #print rtn_df.values
    # print foo.values

def file_output(info, filename):
    col = ['stats']
    # col = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24', 'C25', 'C26']
    # df_info = pandas.DataFrame(info, columns=col)
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