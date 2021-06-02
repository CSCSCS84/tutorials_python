# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
# Not cleaned
import pandas as pd
import numpy as np


scores = pd.read_csv("data//scores.csv")
s=scores.unstack()
print(s.head())
print(type(s))
print(scores.info())
pivoted=scores.pivot(index="School Name",columns="SAT Section",values="Score")
print(pivoted)
print(pivoted.columns)
print(pivoted.index)
print(pivoted.info())
print(pivoted.stack())

piv=scores.pivot_table(index="Borough",values="Student Enrollment",aggfunc=["sum","mean"])
print(piv.head())

queens=scores[scores.Borough=="Queens"]
print(queens)
pi=queens.pivot_table(index="School Name",columns=["SAT Section"],values="Score")
print(pi.info())
print(pi.head())