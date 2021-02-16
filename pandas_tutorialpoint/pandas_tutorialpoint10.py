import pandas as pd

#categorial data are data that can only take a limited number of values, like gender, country etc.
s = pd.Series(["a","b","c","a"], dtype="category")
print (s)

print(pd.Categorical(["a","b","c"]))

#ordered:
ordered=pd.Categorical(["c","b","a"], ordered=True)
print(ordered)
df=pd.DataFrame({"cat":ordered})
print(df["cat"].describe())

#get the categories
print(ordered.categories)

#rename categories
ordered.categories=["Group %s" % s for s in ordered.categories]
print(ordered)

#add categories
s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print(s)

s.cat.remove_categories("a")


