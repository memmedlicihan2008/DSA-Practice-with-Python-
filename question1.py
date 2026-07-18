arr = list(map(int, input().split()))
x=int(input())
k=0
for i in range(0,len(arr)):
    if arr[i]==x:
        print(i)
        k+=1
if k==0:
    print(-1)