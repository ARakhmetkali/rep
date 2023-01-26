a = input()
b = 0
i = 0
while len(a) > i:
    if (a[i] == "i") or (a[i] == "o") or (a[i] == "a") or (a[i] == "e"):
        b = b+1
    i = i +1
print(b)