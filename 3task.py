a = input()
i  =0
j = 0
b = 1
while len(a) > i:
    while len(a) > j:
        if a[i] == a[j]:
            b = b + 1
            del a[j]
        j += 1

    print (a[i]+ "->" + str(b))
    b = 0
    i += 1