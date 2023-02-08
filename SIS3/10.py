def python(a):
    new =[]
    for i in a:
        if i not in new:
            new.append(i)
    return new

print(python([1,2,4,0,0,7,5]))