# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

liberal = pd.read_csv("data//liberal_arts.csv")
state = pd.read_csv("data//state.csv")


#state_and_liberal = pd.concat([state, liberal])
#print(state_and_liberal["School Name"].nunique())
#print(state_and_liberal.info())

#print(state_and_liberal.agg("mean"))

print(state.info())
print(liberal.info())
dfm = pd.merge(state, liberal,how="outer")
print(dfm)
