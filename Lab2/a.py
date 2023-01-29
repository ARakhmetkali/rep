#LIST
#1. Second item
fruits = ["apple", "banana", "cherry"]
print(fruits[1])


#2. Changing the value
fruits = ["apple", "banana", "cherry"]
fruits[0] = "Kiwi"


#3. Using the APPEND to add the value
fruits = ["apple", "banana", "cherry"]
fruits.append("pineapple")


#4. insert
fruits = ["apple", "banana", "cherry"] 
fruits.insert(1, "limon")


#5. remove
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)


#6. negative index to print the last item in the list
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#output: cherry


#7.  range of index
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


#8.  number of items( len() )
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(fruits))