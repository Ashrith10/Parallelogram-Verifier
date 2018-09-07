#Copyright Ashrith Kanakanala 2018
import sys

print("Point D in a Parallelogram Calculator")
print("By Ashrith & Aiyan")
print("Please enter your cords as 'x1,y1'")

cord1 = str(input("Coordinate 1 "))

cord2 = str(input("Coordinate 2 "))

cord3 = str(input("Coordinate 3 "))

x1,y1 = cord1.split(",")
x2,y2 = cord2.split(",")
x3,y3 = cord3.split(",")

x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)


try:
    slope21 = (y2 - y1)/(x2 - x1)
except ZeroDivisionError:
    slope21 = "undefined"

try:
    slope32 = (y3 - y2)/(x3 - x2)
except ZeroDivisionError:
    slope32 = "undefined"


if slope21 == slope32:
    sys.exit("These Coordinates Don't Form a Parallelogram :(")
else:
    midpoint1x = (x1 + x3)/2
    midpoint1y = (y1 + y3)/2

    answerx = (2 * midpoint1x) - x2
    answery = (2 * midpoint1y) - y2

    print("(",answerx,",",answery,")")
