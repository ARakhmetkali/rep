#1
square = (i * i for i in range(int(input())+1))
for i in square:
    print(i, end=" ")
print("\n")


#2
n=int(input())
even = (i for i in range(0, n+1) if i % 2 == 0)
for i in even:
    print(i, end=", ")


#3
print("\n")
h= int(input())
div = [i for i in range(0, h+1) if i%3 == 0 and i%4 == 0]
for i in div:
    print(i, end=" ")
print("\n")


#4
squares_generator = (i * i for i in range(int(input()), int(input())))
for i in squares_generator:
    print(i)


#5
k = int(input())
down=[i for i in range(0, k +1)]
for i in reversed(down):
    print(i,end=" ")