def firstoccurrenceinsorted(arr,k):
   
    for i in arr:
        if i==k:
            c=arr.index(i)
            return c 
    return -1
arr=list(map(int,input().split())) 
k=int(input()) 
print(firstoccurrenceinsorted(arr,k))
