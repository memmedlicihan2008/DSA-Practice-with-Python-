s=list(input())
t=list(input())
k=0
if len(s)==len(t):
    for i in s:
        if s.count(i)!=t.count(i):
            print(False)
            k+=1
            break
    if k!=1:
        print(True)
else:
    print(False)


