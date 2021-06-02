# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
# Not cleaned
import pandas as pd

liberal = pd.read_csv("data//liberal_arts.csv")
state = pd.read_csv("data//state.csv")

print(state.info())
print(liberal.info())
dfm = pd.merge(state, liberal,how="outer")
print(dfm)
