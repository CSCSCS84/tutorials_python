import random

print("This line will be printed.")

if 5 > 2:
    print("Five is greater t  han two!")

# this is a comment


"""
sdffha
"""

a, b, c = "hello", "b", "c"
print(a)
print(b)
print(c)
print("python is " + c)


def firstmethod(x):
    global y
    y = "hello"
    print(x)


firstmethod("hallo")


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

x = 3 + 1j
print(type(x))

f = 3.5E10
print(f)

print(random.randrange(1, 10))

print(f"{x} {f}")
