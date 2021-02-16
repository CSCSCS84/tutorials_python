import pandas as pd
import numpy as np
data=np.array(["a","b","c"])
s=pd.Series(data,index=[0,1,5])
dict = {"a": 1, "b": 2}
s2 = pd.Series(dict)
print(s2["b"])
print(s2)
s3=pd.Series(4,index=[1,24,3])
print(s3[24])
data=[1,2,3,4,5]
dt=pd.DataFrame(data,index=[0,1,2,3,4],columns=["hallo"])
data = [['Alex',10],['Bob',12],['Clarke',13]]
print(len(data))
df = pd.DataFrame(data,columns=['Name','Age'])
print(data)
print(dt)

data=[{"name":["jil","kl"],"age":[2,4]},{"name":["anne"],"g":["w"]}]
df=pd.DataFrame(data)
print(df)
print()
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'd']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df["new"]=pd.Series(["gg","ddsaf","asdfsa"],index=["a","b","c"])
print(df)
del(df["two"])
df.pop("new")
print(df)

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
l=df.loc['b']
print (type(l))


s = pd.Series(np.random.randn(4))
print ("The axes are:")
print(s.axes)
print(s.empty)
print(s.ndim)
print(s.size)
print(len(s))
print(s.values)
print(s.head(3))


