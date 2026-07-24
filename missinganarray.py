arr=list(map(int,input().split()))
arr.sort()
for i in arr:
    if 1 in arr:
        if i+1 in arr:
            continue 
        else:
            print(i+1)
            break 
    else:
        print(1)
        break 