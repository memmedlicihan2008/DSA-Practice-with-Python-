def majorityElement(arr):
     #code here
    for i in arr:
        if arr.count(i)>len(arr)/2:
            return i
arr=list(map(int,input().split()))
print(majorityElement(arr))