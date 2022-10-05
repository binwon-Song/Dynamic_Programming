n,m=map(int,input().split())

cnt=0

number=[i for i in range(1,n+1)]
pop_number=list(map(int,input().split()))


while len(pop_number)!=0:
    if pop_number[0]==number[0]:
        number.remove(number[0])
        pop_number.remove(pop_number[0])
    elif len(number)//2<number.index(pop_number[0]):
        number.insert(0,number[-1])
        number=number[:-1]
        cnt+=1  
    else:
        number.append(number[0])
        number=number[1:]
        cnt+=1
print(cnt)