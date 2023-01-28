# print the length of the string.
# Len
x = "Hello World"
print(len(x))


#Get the first character of the string txt
txt = "Hello World"
print(txt[0])


#Get the characters from index 2 to index 4
txt = "Hello World"
x = txt[2:5]
print(x)


#Возвращает строку без пробелов в начале или в конце.
#         Strip
txt = " Hello World "
x = txt.strip()
print(x)


#upper case.
txt = "Hello World"
txt = txt.upper()
print(txt)


#lower case
txt = "Hello World"
txt = txt.lower()
print(txt)


#Replace
txt = "Hello World"
txt = txt.replace("Hello","The")
print(txt)


#Insert the correct syntax to add a placeholder for the age parameter.
# Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))