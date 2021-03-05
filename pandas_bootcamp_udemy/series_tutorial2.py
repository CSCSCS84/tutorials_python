# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

url = "https://gist.githubusercontent.com/sh7ata/e075ff35b51ebb0d2d577fbe1d19ebc9/raw/b966d02c7c26bcca60703acb1390e938a65a35cb/drinks.csv"

s = pd.read_csv(url, usecols=["country", "wine_servings"], index_col="country", squeeze=True)

wine_servings = s.dropna()
# or
wine_servings = s[s.notnull()]
print(wine_servings)
print(wine_servings.sum())
print(wine_servings[wine_servings < 100].sum())

fifyt_plus = wine_servings[wine_servings > 50]
print(fifyt_plus)
fifyt_plus.sort_values(ascending=True, inplace=True)
print(fifyt_plus[:20])
# or
print(fifyt_plus.nsmallest(20))
