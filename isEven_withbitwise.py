def isEven(n):
    if (n & 1):
        return False
    else:
        return True 
n=int(input())
print(isEven(n))
