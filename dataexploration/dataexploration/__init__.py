#### Author: Daphne 
#### comments/suggestions: github.com/daphn3k/data_analysis
#### version 0.1 - 20.06.2019
#### Published under GNU GLP v3.0

import pandas as pd

def find_NaN(df, filename='df_NaN.txt', threshold=100):

    '''  
    Find number of NaN/Null values in pandas dataframe columns, save result to file.

    File will contain name of column, number of missing values & corresponding percentage.
    Also returns dictionary with column name and percentage of missing value, if percentage is over threshold set during call

    Parameters
    ----------
    - df: pandas dataframe to look for NaNs
    - filename: optional. Desired name to give to output file. Default is df_NaN.txt
    - threshold: optional. When percentage of missing values in a column is over threshold, include this column 
                in dict to be returned. Default threshold is 100%, dict will be empty

    Examples
    --------
    >> df = pd.DataFrame({'A': [0, 1, 2, None],
                          'B': [3, None, 5, 6]},
                          'C': [7, 8, 9, 10],
                          'D': [11, None, None, None])
    >> find_NaN(df)
    >>
    contents of df_NaN.txt are: 
        A:  1   25.00%
        B:  1   25.00%
        D:  3   75.00%

    >> nans = find_NaN(df, 10)
        contens of df_NaN.txt are as above
    >> nans
        {'A': 25.0, 'B': 25.0, 'D': 75.0}

    '''
    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    f = open(filename, 'w')
    
    percent = {}
    
    for nans, col in zip(df.isna().sum(), df):
        if nans!=0:
            percentNan = 100*nans/len(df)
            f.write('%s:\t\t%d\t\t%.2f%%\n' % (col, nans, percentNan))
            if percentNan >= threshold:
                percent[col] = percentNan
            
    f.close()

    return percent



def cols_NaN(df, threshold=10):

    '''
    Returns list with names of columns containing percentage of NaN values over the chosen threshold
    
    Parameters
    ----------
    - df: pandas dataframe
    - threshold: when percentage of missing values is over threshold, include this column 
                in dict to be returned. Default threshold is 10%


    Example
    -------
    >> df = pd.DataFrame({'A': [0, 1, 2, None],
                          'B': [3, None, 5, 6],
                          'C': [7, 8, 9, 10],
                          'D': [11, None, None, None]})
    >> cols_to_drop = cols_NaN(df, 50)
    >> cols_to_drop
        ['D']

    '''
    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    columns = [col for nans, col in zip(df.isna().sum(), df) if (nans*100/len(df)) >= threshold]

    return columns

