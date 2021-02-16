import pandas as pd

url = 'https://raw.github.com/pandasdev/pandas/master/pandas/tests/data/tips.csv'

tips = pd.read_csv(url)
# top rows
print(tips.head())
# filter:
print(tips[tips['time'] == 'Dinner'].head(5))
