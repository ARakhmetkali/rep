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
    return f"Uppercases {g}\nLowercases {k}"

def palindrome(s):
    return s == s[::-1]

def wait_before_invoke(x,t):
    time.sleep(t/1000)
    return sqrt(x)

def tuple_elements(a):
    return all(a)