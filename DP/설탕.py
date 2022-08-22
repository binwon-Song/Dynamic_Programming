Total_Sugar=int(input())
# sugar weight is only 3 or 5
f=Total_Sugar//5
for i in reversed(range(f+1)):
    if (Total_Sugar-(i*5))%3==0:
        print(i+(Total_Sugar-(i*5))//3)
        exit()
print(-1)
