#1: 
#correct syntax to import a module
import mymodule

#2: 
#Если вы хотите ссылаться на модуль, используя
#другое имя, вы можете создать псевдоним(alias).
import mymodule as mx


#3:
#printing all variables and function names of the "mymodule" module
import mymodule
print(dir(mymodule))

#4:
from mynodule import person1