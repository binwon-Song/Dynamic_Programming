col=int(input())
a=[0]*(col+1)

if col==1:
    print(3)
elif col==2:
    print(7)
else:
    a[1]=3
    a[2]=7
    for i in range(3,col+1):
        a[i]=(a[i-2]+a[i-1]*2)%9901
    print(a[col])