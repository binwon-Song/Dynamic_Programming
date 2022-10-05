L,R=map(int,input().split())
min_result=2**31
for i in range(L,R+1):
    result=str(i).count('8')
    min_result=min(min_result,result)
    if min_result==0:
        break
print(min_result)
