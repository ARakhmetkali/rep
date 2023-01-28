"""
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
"""
price = 49
txt = "The price is {} dollars"
print(txt.format(price))


"""
You can add parameters inside the curly brackets to specify how to convert the value:

Example
Format the price to be displayed as a number with two decimals:
"""
txt = "The price is {:.2f} dollars"
print(txt.format(price))


#If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


"""
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you
pass the parameter values txt.format(carname = "Ford"):
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))