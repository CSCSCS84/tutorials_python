# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

url = "https://gist.githubusercontent.com/sh7ata/56976975b3c67caabb2efd80bb3a8467/raw/f1b7d2abf6770548edafee58ea15be71e2d28aac/Nutrition.csv"

nutrion = pd.read_csv(url)

nutr_mini = nutrion.sample(10)
print(nutr_mini.columns)
print(nutr_mini.head())
print(nutr_mini[["total_fat", "cholesterol"]])

print(nutr_mini.loc[:, "vitamin_b12":][0:2])
# or
b12_loc = nutr_mini.columns.get_loc("vitamin_b12")
print(nutr_mini.iloc[2, b12_loc])
print(nutr_mini.iat[2, 3])

nutrion.sort_values(by="vitamin_b12", inplace=True, ascending=False)
pd.options.display.max_columns = 10
print(nutrion.head(10))

pd.options.display.min_rows = 1000
food_with_eggplant = nutrion.filter(regex="(?i)eggplant", axis=0)

print(food_with_eggplant)

print(nutrion.sample(n=4, axis=0).sample(n=2, axis=1))

print(nutrion.size)
nutrion.dropna(how="any", axis=0, inplace=True)
print(nutrion.size)

nutrion["vitamin_c"] = nutrion["vitamin_c"].replace("[a-zA-Z]", "", regex=True)

print(nutrion["vitamin_c"].unique())
nutrion["vitamin_c"] = nutrion["vitamin_c"].astype(float)

print(nutrion[nutrion["vitamin_c"].between(20, 40)])
