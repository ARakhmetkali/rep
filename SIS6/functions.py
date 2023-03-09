import time
from math import sqrt

def multiply(l):
    total = 1
    for num in l:
        total *= num
    return total

def upper_lower_case(s):
    g, k = 0, 0
    for leta in s:
        if leta.islower():
            g+=1
        if leta.isupper():
            k+=1
    return f"Uppercases {k}\nLowercases {g}"

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def wait_before_invoke(x,t):
    time.sleep(t/1000)
    return sqrt(x)

def tuple_elements(a):
    return all(a)

#1
l = [1,2,3,4]
print(multiply(l))

#2
l = "Qwerty"
print(upper_lower_case(l))

#3
s = "qwq"
print(palindrome(s))

#4
d = 12344
k = 12311
print(wait_before_invoke(d,k))

#5
a = (5,2,0,"awd")
print(tuple_elements(a))