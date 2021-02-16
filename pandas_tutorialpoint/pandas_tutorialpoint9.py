import pandas as pd

# merging and joining

left = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']})
right = pd.DataFrame(
    {'id': [1, 2, 3, 4, 5],
     'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
     'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']})

print(pd.merge(left, right, on="id"))
print(pd.merge(left, right, on="subject_id", how="left"))
# left: use the left keys, check on the right dataframe if key exist and merge the rows

# inner: only merge if both dataframes have a specific key
print(pd.merge(left, right, on="subject_id", how="inner"))
print("--------")
print(pd.merge(right, left, on="subject_id", how="inner"))
# merge all
print(pd.merge(left, right, on="subject_id", how="outer"))

# concat: is also focused on rows
one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5'],
    'Marks_scored': [98, 90, 87, 69, 78]},
    index=[1, 2, 3, 4, 5])

two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5'],
    'Marks_scored': [89, 80, 79, 97, 88]},
    index=[1, 2, 3, 4, 5])
print(pd.concat([one, two]))
print(pd.concat([one, two], keys=["x", "y"]))

dfconcated = pd.concat([one, two], keys=["x", "y"])
print(dfconcated.loc["x"])
print(type(dfconcated.loc["x"]))

print(pd.concat([one, two], ignore_index=True))
print(pd.concat([one, two], axis=1))

# A useful shortcut to concat are the append instance methods on Series and DataFrame.
# These methods actually predated
# concat. They concatenate along axis=0, namely the index

print(one.append(two))
print(one.append([one, two, two]))

# working with time on panda

print(pd.Timestamp("2013-10-10"))
print(pd.Timestamp(123124231, unit="s"))
print(pd.date_range(start="11:00", end="15:00", freq="30min").time)
print(pd.date_range(start="11:00", end="15:00", freq="H").time)

# convert to datetime
print(pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None])))

# create a range of days
print(pd.date_range(start="2019-11-09", end="2019-12-11", freq="D"))
# or use periods
print(pd.date_range(start="2019-11-09", periods=10, freq="D"))

# bdate excludes Saturday and Sunday
print(pd.bdate_range('1/1/2011', periods=10))

# Offset Aliases like "H" or "D"

# timedelta
print(pd.Timedelta("2 Days"))
print(pd.Timedelta(2, unit="D"))

s = pd.Series([pd.Timedelta(i, unit="D") for i in range(10)])
print(s)
# addition and substraction is possible
print(s[9] - s[7])
