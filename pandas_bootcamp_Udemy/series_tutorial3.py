# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd
import matplotlib.pyplot as plt

url = "https://gist.githubusercontent.com/sh7ata/e075ff35b51ebb0d2d577fbe1d19ebc9/raw/b966d02c7c26bcca60703acb1390e938a65a35cb/drinks.csv"

beer = pd.read_csv(url, usecols=["country", "beer_servings"], index_col="country", squeeze=True)

print(beer.describe())
print(beer.mode())

beer_first10 = beer[:10]

print(beer_first10.divide(beer_first10.mean()))

print(beer_first10.divide(beer_first10.median()))

beer.hist()
plt.show()
