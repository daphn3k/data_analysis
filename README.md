# data_analysis
Collecting my python functions to facilitate data exploration/analysis/etc.
---------------

Available packages:   
** dataexploration **

### Installation of desired package:  
- clone the repo
- in terminal navigate to module folder containing setup.py
- type:  
  > pip install -e .

Feel free to contact me with comments/questions/requests by creating a new issue. 
I'm using semantic versioning.

----------------
v0.2:
*plotting module:*
- **numeric_Hist(args)**: create files with groups of histograms of numeric columns from pandas.Dataframe - Useful to get a quick overview of distributions 

v0.1:
*exploration module:*  
- **read_csv_to_df(args)**: reads csv file to pandas dataframe & add a name attribute to dataframe - Facilitates naming of output files from the other functions of this module
- **find_NaN(args)**: Calculates count and percentage of NaN values in pandas dataframe columns, save result to file. - Useful to get overview of large dataframe with many features
- **col_NaN(args)**: Returns list with names of columns containing NaN values over the chosen percentage threshold. - Useful for dropping columns eg. 'df.drop(col_NaN(df,15), axis=1, inplace=True)' 
- **categoricals(args)**: Saves the categorical fields of a pandas dataframe with their associated values and values count to .txt file & returns it as dict - Useful to get overview of large dataframe with many features
- **export_columns(args)**: Saves the names of a dataframe's columns to txt.file 
- **export_descriptive_stats(args)**: Saves output of pandas.DataFrame.describe() to .csv file 
- **low_variance(args)**: Identify columns that have at least x percent of same values



to do:
* extend read_csv_to_df to include more filetypes 
* add 3d plot for KMeans