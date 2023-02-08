import random
x=(random.randrange(1,20))
print("Hello what's your name?")
a = input()
print()
print("Well, "+ a + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
y = int(input())
k = 1
while y != x:
    print()
    if y < x:
        print("Your guess is  lower.")
    else:
        print("Your guess is  bigger.")
    print("Take a guess.")
    k +=1
    y = int(input())
if y == x:
    print()
    print("Good job, "+ a +"! You guessed my number in " + str(k) + " guesses!")
