def findkthrotation(arr):
    k=0
    for i in range(0,len(arr)-1):
        if arr[i]<arr[i+1]:
            k+=1
        else:
            k=0 
    return len(arr)-(k+1)
arr=list(map(int,input().split()))
print(findkthrotation(arr)) 
