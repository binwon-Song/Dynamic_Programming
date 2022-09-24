N,K=map(int,input().split())
result=0
bi_N=bin(N)[::-1]
if bi_N.count('1')<=K:
    print(0)
else:
    for i in range(bi_N.count('1')-K):    
        result+=2**(bi_N.index('1'))
        bi_N=bi_N.replace('1','0',1)
    print(2**bi_N.index('1')-result)