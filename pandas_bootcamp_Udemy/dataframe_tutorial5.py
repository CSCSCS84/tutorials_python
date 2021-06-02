# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
# Not cleaned
import pandas as pd
import numpy as np

games = pd.read_csv("data//games_sales.csv")
publishers=games.loc[:,["Publisher","Genre","Platform","NA_Sales"]]
gm=games.loc[:,["Publisher","NA_Sales"]]
tr=gm.groupby("Publisher").sum().transform(lambda x:x+2000)
print(tr)


print(publishers.info())
print(publishers.head())
top10=publishers.groupby("Publisher").sum()
print(top10)
print(top10.sort_values(by="NA_Sales",ascending=False).head(10))

print(games.info())
globalSales_perYear=games.groupby(by=["Year"]).agg(GlobalSales=("Global_Sales","sum"))
print(globalSales_perYear.sort_values(by="GlobalSales",ascending=False))

most_in_europe=games.groupby(["Genre","Year","Platform"]).sum()["EU_Sales"].nlargest(1)
print(most_in_europe)

#bb=games.groupby(["Name","Genre","Platform"]).apply(lambda sg:sg.sum()["NA_Sales"]<sg.sum()["JP_Sales"])
b2=games.groupby(["Name","Genre","Platform"]).filter(lambda sg:sg["NA_Sales"].sum()<sg["JP_Sales"].sum())
print(b2)


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two'],
                   'C' : [1, 5, 5, 2, 5, 5],
                   'D' : [2.0, 5., 8., 1., 2., 9.]})

grouped = df.groupby('A')
print(df)
for name,group in grouped:
    print(group)
g=grouped.transform(lambda x: x.max() - x.min())
print(g)

print(grouped.apply(sum))