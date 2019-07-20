# data_analysis
Collecting my python functions to facilitate data exploration/analysis/etc.
---------------

Available modules: 
* dataexploration

Installation of desired module:  
- clone the repo
- in terminal navigate to module folder containing setup.py
- type:  
  > pip install -e .

Feel free to contact me with comments/questions/requests

----------------
v0.1:  
- find_NaN(): Calculate count and percentage of NaN values in pandas dataframe columns, save result to file. - Useful to get overview of large dataframe with many features
- col_NaN(): Returns list with names of columns containing NaN values over the chosen percentage threshold - Useful for dropping columns eg. 'df.drop(col_NaN(df,15), axis=1, inplace=True)' 
