# Skill Challenges for Udemy course: The Ultimate Pandas Bootcamp: Advanced Python Data Analysis
import pandas as pd

pd.options.display.min_rows = 50

s = pd.Series(data=[1, 2, 4], index=["{}".format(i) for i in range(3)])

print(s.get(["1", "2"]))

squares = pd.Series(data=[i ** 2 for i in range(100)], index=["l{}".format(i) for i in range(100)])
print(squares)
print(squares[-3:])
print(squares.tail(3))
s1 = squares[-3:]
s2 = squares.tail(3)

print(s1.equals(s2))

print("some loc basics")
print(squares["l1":"l10"])
# betrachtet die Werte der Serie
print(squares[squares > 1000])


def fun(x):
    return ["l1", "l10"]


print(squares.loc[fun])


def fun2(x):
    return [1, 2, 4]


print(squares.iloc[fun2])
print(squares.iloc[[True if x % 2 == 0 else False for x in range(100)]])

print(squares.get("l1"))
print(squares.get(["l1", "l11", "l200"], default="Object nicht gefunden"))
