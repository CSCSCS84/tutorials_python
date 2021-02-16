import pandas as pd
import numpy as np
#loc, iloc, ix indexing
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print (df.loc[:,'A'])
#column and row selecting
print(df.loc["a",['A',"C"]])

#print a range of rows and columns
print(df.loc["a":"h","B":"D"])

print(df.loc['a']>0)

#iloc is purely integer based
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df.iloc[2,0:2])

#Besides pure label based and integer based, Pandas provides a hybrid method
#for selections and subsetting the object using the .ix() operator.
#ix is deprecated!!

#statistical functions:
s = pd.Series([1,2,3,4,5,4])
#This function compares every element with its prior element and computes the change percentage
print(s.pct_change())

s1=pd.Series(np.random.randn(1000))
s2=pd.Series(np.random.randn(1000))
print(s1.cov(s2))

#ranking
s1=pd.Series(np.random.randn(5),index=list("abcde"))
s1["a"]=s1["d"]
print(s1.rank())

#For working on numerical data, Pandas provide few variants like rolling, expanding
# and exponentially moving weights for window statistics.
# Among these are sum, mean, median, variance, covariance, correlation, etc.

#rolling average for exampel
r=pd.DataFrame([1,2,3,4,5,6,7])
#average of the last two elements
print(r.rolling(window=2).mean())
#die letzten 2 Perioden kommen dazu
print(r.expanding(min_periods=2).mean())

#ewm function
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.ewm(com=0.5).mean())


#aggregate

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)
print (r.aggregate(np.sum))

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df)
r = df.rolling(window=3,min_periods=1)

#minimum und summe für A ausrechnen und ausgeben
print (df["A"].aggregate(["sum","min"]))
print (df[['A','B']].aggregate([np.sum,np.mean]))
#aggregate using different functions
print(df.aggregate({"A":np.sum,"B":np.mean}))


#missing data
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)
#check for missing data
print(df.isnull())
print(df.notnull())

#using sum, missing data will be treated as zero, except all data ara NaN

#fill data with a value
print(df.fillna(0))

#use data of last row
print(df.fillna(method="pad"))
#use data of next row
print(df.fillna(method="backfill"))

#drop rows with missing data
print(df.dropna())

df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
#replace 2000 with 10
print(df.replace({2000:10}))
