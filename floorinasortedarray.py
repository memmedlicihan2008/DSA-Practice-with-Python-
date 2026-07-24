def floorinasortedarray(arr,k):
    import bisect
    c=[]
    for i in arr:
        if i<=k:
            c.append(i)
    if len(c)>0:
        return bisect.bisect(arr,max(c))-1
    else:
        return -1
arr=list(map(int,input().split()))
k=int(input()) 
print(floorinasortedarray(arr,k))
