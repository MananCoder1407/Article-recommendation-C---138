import pandas as pd;
import numpy as np;

# reading both csv files 
data1 = pd.read_csv('/Users/mananjain/Desktop/Articles Python/data1.csv');
data2 = pd.read_csv('/Users/mananjain/Desktop/Articles Python/data2.csv');

# printing the heads
print(pd.DataFrame.head(data1));
print(pd.DataFrame.head(data2));