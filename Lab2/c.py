"""
set
"""
#1.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")


#2. add element( not append)
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


#3. method to add multiple items (more_fruits) to the fruits set(update).
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


#4. remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")


#5. discard  (to remove "banana" from the fruits set.)
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")