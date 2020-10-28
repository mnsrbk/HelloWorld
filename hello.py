import sys
import requests
import os
import math

print(sys.version)
print(sys.executable)
print("Hello     World !!!")  # this text is comment
age = 20
name = "Mansurbek"
print("{0} was {1} years old when he wrote this book".format(name, age))
print("Why is {0} playing with that python?".format(name))
print("{} was {} years old when he wrote this book".format(name, age))
print("Why is {} playing with that python?".format(name))
# decimal (.) precision of 3 for float '0.333'
print("{0:.3f}".format(1.0 / 3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print("{0:_^90}".format("Project_X"))
# keyword-based 'Swaroop wrote A Byte of Python'
print("{0} wrote {book}".format(name, book="A Byte of Python"))
r = requests.get("http://ariator.com/en")
print(r.status_code)
a = 0
sum = 0
for a in range(20):
    if (a % 3 == 0) & (a % 2 == 0):
        print(a)
    a += a
    sum += a

print(sum)
