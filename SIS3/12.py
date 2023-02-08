def histogram(t):
    k = ""
    for i in range(len(t)):
        for j in range(t[i]):
            k += "*"
        print(k)
        k = ""

histogram([4, 9, 7])