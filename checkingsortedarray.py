arr=list(map(int,input().split()))
k=0
for i in range(0,len(arr)-1):
    if arr[i]>=arr[i+1]:
        k+=1
if k==0:
    print("This array is sorted")
else:
    print("This array is not sorted") 