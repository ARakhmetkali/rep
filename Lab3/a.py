#Ex1:

def my_function():
    print("Hello from a function")


#Ex2: Execute a function named my_function.
def my_function():
  print("Hello from a function")
my_function()


#Ex3: Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)


#Ex4: return
def my_function(x):
    return x + 10


#Ex5: *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


#Ex6:  **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])