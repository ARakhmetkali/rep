from itertools import permutations
def per(s):
    ans=list(permutations(s))
    for i in ans:
        print(str().join(i),end=" ")
s = input()
print(per(s))


# import itertools
 
# val = input()
 
# perm_set = itertools.permutations(val)
 
# for i in perm_set:
#     print(i, end= " ")
