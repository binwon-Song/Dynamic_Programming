import sys,copy
input=sys.stdin.readline
T=int(input())
p=0
for i in range(T):
    k=int(input())
    n=int(input())
    result=[i for i in range(1,n+1)]
    for j in range(k-1):
        tmp=copy.deepcopy(result)
        for p in range(1,n+1):
            result[p-1]=sum(tmp[:p])
    print(sum(result))