#Ex1: Create a class:
class my_name_is_Ayan:
    Ayan = 4


#Ex2: Create an object
class MyClass:
    x = 5

p1 = MyClass()


#Ex3: Use the p1 object to print the value of x
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)


#Ex4:  __init__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
# Используйте функцию __init__() для присвоения значений 
#свойствам объекта или других операций, которые необходимо 
#выполнить при создании объекта:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#Extra ex: __str__()
"""
Функция __str__() управляет тем, что должно быть возвращено, 
когда объект класса представлен в виде строки
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



#return f"{self.name}({self.age})"