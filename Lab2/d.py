"""
Dict
"""
#1 Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


#2. change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


#3. Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


#4. Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#5. Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()