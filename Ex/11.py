def palindrome(f):
    a = f[::-1]
    if f == a:
        return True
    else:
        return False
    
print(palindrome("mada"))