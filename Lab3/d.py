#1: 
#Каков правильный синтаксис для создания класса с именем Student, 
#который будет наследовать свойства и методы от класса с именем Person?
class Student(Person):

#2:
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()