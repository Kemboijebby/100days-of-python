import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = pd.Series(range(1,10))
b = pd.Series(["I","would","like","use","python","and","pandas","for","data"],index=range(0,9))
print(a,b)

#dataframes : frame data in rows  and columns
df=pd.DataFrame([a,b])
#Transforming data
df1=df.T.rename(columns={0:"A",1:"B"})
#print(df1)
#Retrieving values from a dataframe
df2=df1[(df1["A"]<5)]
#print(df2)

#Adding a new column to a table
df1["Mean"]=df1["A"]-df1["A"].mean()
print(df1)



