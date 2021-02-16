import pandas as pd
import numpy as np

df = pd.read_csv("pandas_tutorial.csv", index_col="S.No", dtype={"Salary": np.float64})
print(df)
df = pd.read_csv("pandas_tutorial.csv", dtype={"Salary": np.float64}, names=["a", "b", "c", "d", "e"])
print(df)
# remove header
df = pd.read_csv("pandas_tutorial.csv", dtype={"Salary": np.float64}, names=["a", "b", "c", "d", "e"], header=0)
print(df)

# skiprows
df = pd.read_csv("pandas_tutorial.csv", dtype={"Salary": np.float64}, names=["a", "b", "c", "d", "e"], skiprows=2)
print(df)
print("---------------------------")
# using If/Truth with pandas:
s = pd.Series([True, False, True])
if s.any():
    print("True")
else:
    print("False")
if s.all():
    print("True")
else:
    print("False")

# To evaluate single-element pandas objects in a Boolean context, use the method .bool()
print(pd.Series([True]).bool())

# bitwise boolean
s = pd.Series(range(5))
print(s == 4)

# isin operation
s = pd.Series(list("abc"))
print(s.isin(list("abe")))

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
                                                  'four'], index=list('abcdef'))

print(df)
print(df.reindex(['b', 'c', 'e']))
