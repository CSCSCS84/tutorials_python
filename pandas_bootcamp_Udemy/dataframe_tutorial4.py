# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

tech_giants = pd.read_csv("data//tech_giants.csv", index_col=["date", "name"])
print(tech_giants.info())
print(tech_giants.head())

tech_df2 = tech_giants.loc[(slice("2015-07-13", "2016-08-17"), slice(None))]
tech_df2_xs = tech_giants.xs(slice("2015-07-13", "2016-08-17"), level=(0))

print(tech_df2)
aapl = tech_df2.loc[(slice(None), "AAPL"), :]
aapl_xs = tech_df2.xs(("AAPL"), level=(1))
print(aapl.sample(10))

ex3 = tech_df2.loc[(slice(None), ["AAPL", "GOOGL"]), ["low", "high"]]
print(ex3)

# year month day
tech_df3 = tech_df2.set_index(["year", "month", "day"])
print(tech_df3.head())
print(tech_df3.loc[(2015, slice(None), slice(None))])

tech_series = tech_df3.stack()
print(tech_series.loc[(slice(None), slice(None), slice(None), "close")].mean())

print(tech_series.loc[(slice(None), slice(None), slice(None), "close")].std())
