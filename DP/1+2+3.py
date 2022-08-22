def c(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        a=[0]*n
        a[0]=1;a[1]=2;a[2]=4
        for i in range(3,n):
            a[i]=a[i-1]+a[i-2]+a[i-3]
        return a[n-1]    
number=int(input())
for i in range(number):
    result=c(int(input()))
    print(result)