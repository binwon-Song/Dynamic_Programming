N=int(input())
number=list(map(int,input().split()))
flag=True;result=0
for i in number:
    for j in range(2,i):
        if i%j==0:
            break
            flag=False
    if flag==True:
        result+=1
        
