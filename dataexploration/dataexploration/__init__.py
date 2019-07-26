#### Author: Daphne 
#### comments/suggestions: github.com/daphn3k/data_analysis
#### version 0.1 - 26.06.2019
#### Published under GNU GLP v3.0

import pandas as pd
import pandas.io


def set_filename(dataframe, filename, default:str):
    '''Generate the filename that will be used by other functions in this module to save their output

    Parameters:
    -----------
    - dataframe {pandas.Dataframe} -- [dataframe.name value]
    - filename {str} -- [optionally provided by user]
    - default {str} -- [what to use if filename and dataframe.name are not provided]
    
    Returns:
    --------
    - {string} -- [If filename provided by used - return this
        If not, but dataframe has a value for the .name attribute, return string with these components: .name_default
        If dataframe has no associated name return default]

    Examples:
    --------
    >> test_dataframe = pandas.DataFrame({'A': [0, 1, 2, None],
                          'B': [3, None, 5, 6]},
                          'C': [7, 8, 9, 10],
                          'D': [11, None, None, None]})

    >> output = set_filename(test_dataframe, filename=None, 'NaN.txt')
    >> output
    >> 'NaN.txt'
    .......
    >> test_dataframe.name = 'test'
    >> output = set_filename(test_dataframe, filename=None, 'NaN.txt')
    >> output
    >> 'test_NaN.txt'
    .......
    >> output = set_filename(test_dataframe, 'outputName.txt', 'NaN.txt')
    >> output
    >> outputName.txt    


    '''
    if type(dataframe) != pd.DataFrame: raise ValueError("input not pandas DataFrame, can't set filename")

    if type(filename) == str:
        fn = filename
    else:
        try:
            fn = '%s_%s' % (dataframe.name, default)
        except:
            fn = default
    return fn


def read_csv_to_df(path, name='dataframe'):
    ''' 
    read csv file to pandas dataframe & add a name to dataframe
    
    Parameters:
    ----------
    - path {str}: path of df
    - name {str}: sets the dataframe.name value - Useful for generating text file names [default:{'dataframe'}]
    - row_with_column_names {str}: the input for pandas.read_csv 'header' parameter [default:{None}]

    Returns:
    --------
    pandas.DataFrame 
    
    Comment: 
    --------
    Providing a 'name' is advised, if you're planning to use more functions from the dataexploration module. 
    '''
    
    df = pandas.read_csv(path)
    df.name = name
    
    return df



def find_NaN(df, filename=None, threshold=100):

    '''  
    Find number of NaN/Null values in pandas dataframe columns, save result to file.

    File will contain name of column, number of missing values & corresponding percentage.
    Also returns dictionary with column name and percentage of missing value, if percentage is over threshold set during call

    Parameters
    ----------
    - df {pandas.DataFrame}: where to look for NaNs
    - filename {str}: optional. Name to assign to file. Can also be a full path eg. ../output/test.txt
         If filename provided, this will be used to save output, if dataframe.name has a value then the default value is attached to it, 
        if neither conditions are met, default is used. [Default: {NaN.txt}]
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
    contents of NaN.txt are: 
        A:  1   25.00%
        B:  1   25.00%
        D:  3   75.00%

    >> nans = find_NaN(df, 10)
        contens of NaN.txt are as above
    >> nans
        {'A': 25.0, 'B': 25.0, 'D': 75.0}

    '''
    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    # generate name of file to save output
    filename = set_filename(df, filename, 'NaN.txt')

    f = open(filename, 'w')
    
    percent = {}
    
    spaces = max([len(el) for el in df.columns]) # max character length of column names. Will be used for allignment of columns 

    for nans, col in zip(df.isna().sum(), df):
        if nans!=0:
            percentNan = 100*nans/len(df)
            f.write('%s%s:\t\t%.2f%%\t\t%d\n' % ((' '*(spaces-len(col))), col, percentNan, nans))
            if percentNan >= threshold:
                percent[col] = percentNan
            
    f.close()

    return percent



def cols_NaN(df, threshold=10):

    '''
    Returns list with names of columns containing percentage of NaN values over the chosen threshold
    
    Parameters
    ----------
    - df {pandas.DataFrame}: Your data
    - threshold {int of float}: when percentage of missing values is over threshold, include this column 
                in dict to be returned. [default: {10%}]

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



def categoricals(df, filename = None):
    '''Saves the categorical fields of a pandas dataframe with their associated values and values count to .txt file
    
    Parameters:
    ----------
    - df {pandas dataframe} -- Your data
    - filename {str} -- [optional. Name to assign to file. Can also be a full path eg. ../output/test.txt
        If filename provided, this will be used to save output, if dataframe.name has a value then the default value is attached to it, 
        if neither conditions are met, default is used. (default: {'categorical.txt'})
    
    Returns:
    --------
    [dictionary] -- [key: Fields, value: [dictionary -- key: field category, value: field category values count]]
    
    
    Example
    -------
    >> df = pd.DataFrame({'A': [0, 1, 2, None],
                          'B': ['big', 'medium', 'tiny', 'small'],
                          'C': [7, 8, 9, 10],
                          'D': ['yes', 'no', 'yes', 'yes']})
    >> cat = categorical(df)
    >> cat
        {'B':   {'tiny': 1, 
                'small': 1, 
                'big': 1, 
                'medium': 1}, 
        'D':    {'yes': 3, 
                'no': 1}}

    contents of categorical.txt are:
        ***B***
        medium: 1
         small: 1
          tiny: 1
           big: 1

        ***D***
        yes:    3
         no:    1


    '''
    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    # generate name of file to save output
    filename = set_filename(df, filename, 'categorical.txt')

    # create dict with values of categorical fields
    categorical = {}
    spaces = {}

    for el in df:
        if df[el].dtype == 'O': # 'O' for type object
            categorical[el] = {k:v for k, v in zip(df[el].value_counts().keys(), df[el].value_counts().values)}  
            spaces[el] = max([len(word) for word in categorical[el].keys()]) # max character length of feature names. Will be used for allignment of columns
    
    # save categorical dict to file
    g = open(filename, 'w')
    for key, val in categorical.items():
        g.write('***' + str(key) + '***\n')
        for feat, numb in val.items():
            g.write('%s%s:\t%s\n' % ((' '*(spaces[key]-len(feat))), str(feat),str(numb)))
        g.write('\n')
    g.close()

    return categorical 



def export_columns(df, filename = None):
    '''Save the names of a dataframe's columns to .txt file
    
    Parameters:
    -----------
    - df {pandas.DataFrame} 
    - filename {str} -- [Optional. Name to assign to file. Can also be a full path eg. ../output/test.txt
        If filename provided, this will be used to save output, if dataframe.name has a value then the default value is attached to it, 
        if neither conditions are met, default is used. [default: {'columnsName.txt'}]
    '''

    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    # generate name of file to save output
    filename = set_filename(df, filename, 'columnsName.txt')

    c = open(filename, 'w')
    for el in df.columns:
        c.write('%s \n' % el)
    c.close()
    return 



def export_descriptive_stats(df, filename = None):
    '''Save output of pandas.DataFrame.describe() to .csv file 
    
    Arguments:
    - df {pandas.DataFrame} 
    - filename {str} -- [Optional. ame to assign to file. Can also be a full path eg. ../output/test.txt
        If filename provided, this will be used to save output, if dataframe.name has a value then the default value is attached to it, 
        if neither conditions are met, default is used. [default: {'descriptiveStats.csv'}]
    '''

    if type(df) != pd.DataFrame: raise ValueError('input not pandas DataFrame')

    # generate name of file to save output
    filename = set_filename(df, filename, 'descriptiveStats.csv')

    d = open(filename, 'w', newline='') # examine descriptive statistics 
    df.describe().to_csv(filename)
    d.close()
    return



