arr=list(map(int,input().split()))
k=0
for i in arr:
    if arr.count(i)>1:
        k+=1
if k>=1:
    print(True)
else:
    print(False)

