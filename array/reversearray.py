arr = list(map(int, input().split()))
c=[]
for i in range(len(arr) - 1, -1, -1):
    c.append(arr[i])
print(c)
