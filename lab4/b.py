#1
def myfunc():
  x = 300
  print(x)

myfunc()


#2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#3. Global
x = 300

def myfunc():
  print(x)

myfunc()

print(x)


#4
"""
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
one available in the global scope (outside the function) and one available in the local scope (inside the function):

"""
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


#5
"""
If you use the global keyword, the variable belongs to the global scope:
"""
def myfunc():
  global x
  x = 300

myfunc()

print(x)


#6
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)