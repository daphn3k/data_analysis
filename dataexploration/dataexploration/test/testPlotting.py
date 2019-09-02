import sys
sys.path.append("..")
import random
import pandas as pd
from plotting import *

df = pd.DataFrame({'a':[random.randint(100,500) for i in range(0,100)], 
                   'b':[random.randint(0,50) for i in range(0,100)], 
                   'c':[random.randint(10000,50000) for i in range (0,100)], 
                   'd':[random.randint(400,420) for i in range(0,100)],  
                   'e':[random.randint(300,310) for i in range(0,100)], 
                   'f':[random.randint(20,30) for i in range(0,100)], 
                   'ab':[random.randint(200,500) for i in range(0,100)],  
                   'bb':[random.randint(0,20) for i in range(0,100)],  
                   'cb':[random.randint(100000, 110000) for i in range (0,100)],  
                   'db':[random.randint(360,420) for i in range(0,100)],   
                   'eb':[random.randint(300,610) for i in range(0,100)],  
                   'fb':[random.randint(50,80) for i in range(0,100)], 
                   'ax':[random.randint(100,500) for i in range(0,100)],  
                   'bx':[random.randint(0,50) for i in range(0,100)],  
                   'cx':[random.randint(10000,50000) for i in range (0,100)],  
                   'dx':[random.randint(400,420) for i in range(0,100)],   
                   'ex':[random.randint(300,310) for i in range(0,100)],  
                   'fx':[random.randint(20,30) for i in range(0,100)], 
                   'ma':[random.randint(100,500) for i in range(0,100)],  
                   'mb':[random.randint(0,50) for i in range(0,100)],  
                   'mc':[random.randint(10000,50000) for i in range (0,100)],  
                   'md':[random.randint(400,420) for i in range(0,100)],   
                   'me':[random.randint(300,310) for i in range(0,100)],  
                   'mf':[random.randint(20,30) for i in range(0,100)] 
                   })        

numeric_Hist(df, path='output/')
numeric_Hist(df, bins=10, color = 'purple', plotCols = 5, path='output/')  