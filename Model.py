__author__ = 'Hadoop'

from sklearn.linear_model import LogisticRegression, LinearRegression
import pandas;
import os;
import numpy;
import statsmodels
import scikits.statsmodels
from statsmodels.regression.linear_model import OLS
file_loc = '/Users/Hadoop/Documents/Kaggle/Display_Advertising_Challenge/train/sub'



def logistic_reg():
    for subdir, dirs, files in os.walk(file_loc):
        for file in files:
            if file != '.DS_Store' and file != '.testinput.swp':
                if file.endswith('aa'):
                    header = ['Id','Label','I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I13','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24','C25']
                    df_header = pandas.read_csv(file_loc+'/'+file, sep=',', nrows=1)
                    f = pandas.read_csv(file_loc+'/'+file, sep=',', skiprows=1, header=None, names=header)
                else:
                    f = pandas.read_csv(file_loc+'/'+file, sep=',', header=None, names=header)

                Y = f['Label']
                colname = [x for x in f.keys() if 'I' in x and 'Id' not in x]
                X = numpy.array(f[colname].values, dtype = numpy.float)



                logit = LogisticRegression(C=1.0)
                #Learn LogReg
                logit.fit(X,Y)
                # print logit.coef_

                predicted = logit.predict(X)
                error = sum([abs(float(Y[i]) - float(predicted[i])) for i in range(len(Y))])

                X_header = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I13']
                print file
                for i in range(X.shape[1]):

                    # print statsmodels.stats.outliers_influence.variance_inflation_factor(X,i)

                    print '     ', variance_inflation_factor(X, i, X_header[i])
                # print error



def variance_inflation_factor(exog, exog_idx, header):
    '''variance inflation factor, VIF, for one exogenous variable

    The variance inflation factor is a measure for the increase of the
    variance of the parameter estimates if an additional variable, given by
    exog_idx is added to the linear regression. It is a measure for
    multicollinearity of the design matrix, exog.

    One recommendation is that if VIF is greater than 5, then the explanatory
    variable given by exog_idx is highly collinear with the other explanatory
    variables, and the parameter estimates will have large standard errors
    because of this.

    Parameters
    ----------
    exog : ndarray, (nobs, k_vars)
        design matrix with all explanatory variables, as for example used in
        regression
    exog_idx : int
        index of the exogenous variable in the columns of exog

    Returns
    -------
    vif : float
        variance inflation factor

    Notes
    -----
    This function does not save the auxiliary regression.

    See Also
    --------
    xxx : class for regression diagnostics  TODO: doesn't exist yet

    References
    ----------
    http://en.wikipedia.org/wiki/Variance_inflation_factor

    '''
    k_vars = exog.shape[1]
    x_i = exog[:, exog_idx]
    mask = numpy.arange(k_vars) != exog_idx
    x_noti = exog[:, mask]
    r_squared_i = OLS(x_i, x_noti).fit().rsquared
    vif = 1. / (1. - r_squared_i)
    return header, vif

def main():
    logistic_reg()




if __name__ == '__main__':
    main()
