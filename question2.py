arr=list(map(int,input().split()))
x=0
for i in range (0,len(arr)):
    if arr[i]>x:
        x=arr[i]
print(x)
