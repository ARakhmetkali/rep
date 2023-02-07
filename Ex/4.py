def filter_prime():
    b = input().split()
    a = list(map(int, b))
    i = 0
    print("prime numbers:", end =" ")
    while len(a) > i:
        k=2
        l = 0
        m = 0
        q = len(a)
        while a[i] >= k:
            if (a[i] % k == 0) and (a[i] != k):
                l=1
            elif (a[i] == k) and  (l != 1):
                m = 1
            k = k +1
        if (m == 1) and (i != q):
            print(str(a[i]), end = " ")
        m = 0
        i = i +1
filter_prime()
