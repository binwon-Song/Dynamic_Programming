import sys
import copy
def fibo(n):
    zero=[1,0];one=[0,1]
    tmp1=zero
    tmp2=one
    new=[0]*2
    if n==0:
        return zero
    elif n==1:
        return one
    else:
        for i in range(2,n+1):
            new[0]=tmp1[0]+tmp2[0]
            new[1]=tmp1[1]+tmp2[1]
            tmp1[:]=tmp2[:];tmp2[:]=new[:]            
        return new
number=int(sys.stdin.readline())

for i in range(number):
    a=fibo(int(sys.stdin.readline()))
    print(a[0],a[1])