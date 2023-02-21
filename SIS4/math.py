#1
import math
x = int(input("Input degree: "))
print("Output radian:", end=" ")
print(math.radians(x))


#2
def trap():
    h = int(input("Height: "))
    b1 = int(input("Base, first value: "))
    b2 = int(input("Base, second value: "))
    print("Expected Output:", end=" ")
    print(((b1 + b2)*h)/2)
trap()


#3
from math import tan,pi 
def Polygon(): 
    sides = int(input("Input number of sides: ")) 
    len = int(input("Input the length of a side: "))
    Area = (len ** 2 * sides) / 4 * tan(pi / sides) 
    print("The area of the polygon is: ", end="")
    print(Area)

Polygon()


#4
def parallelogram():
    l = int(input("Length of base: "))
    h = int(input("Height of parallelogram: "))
    print("Expected Output: ", end="")
    print(l*h)
parallelogram()
