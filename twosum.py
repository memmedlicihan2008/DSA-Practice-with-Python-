arr = list(map(int, input().split()))
t=int(input())
c=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==t:
            c.append(i)
            c.append(j)
            break
print(c)
