import pandas as pd
import numpy as np

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
dTranspose = df.T
print(df)
print(df.axes)
print(dTranspose.axes)
print(df.dtypes)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.values)

d = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack',
                        'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])
     }

# Create a DataFrame
df = pd.DataFrame(d)
print(df.std(axis=0))
print(df.mode())
print(df.describe(include="all"))


def adder(ele1, ele2):
    return ele1 + ele2


df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df)
df.pipe(adder, 2)
print(df.apply(np.mean, axis=1))
print(df.apply(lambda x: x.max() - x.min()))
print(df["col1"].map(lambda x: x * x))
print(df)

N = 20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
df_reindex = df.reindex(index=[0, 2, 5], columns=["x", "D"])
print(df_reindex)

df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])

df2_reindex = df1.reindex_like(df2)
print(df2_reindex)

df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['col1', 'col2', 'col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1, method='ffill', limit=1))

print(df1.rename(columns={'col1': 'c1', 'col2': 'c2'},
                 index={0: 'apple', 1: 'banana', 2: 'durian'}))
