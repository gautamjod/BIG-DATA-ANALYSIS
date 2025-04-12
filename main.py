import dask.dataframe as dd
import pandas as pd


#Load data in dataframe
df=dd.read_csv('Salesdata.csv',assume_missing=True)

#display first 5 rows
print(df.head())

#Handling missing values
df['Amount']=df['Amount'].fillna(df['Amount'].mean())
df['Review']=df['Review'].fillna(df['Review'].mean())

#convert data to proper format
df['Date']=dd.to_datetime(df['Date'],format='%d,%m,%Y')

print(df.isnull().sum().compute())
#save cleaned data
df.to_csv('Cleaned.csv',index=False)


