n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(m):
    xy=(list(map(int,input().split())))
    result=0
    for j in range(xy[2]-xy[0]+1):
        y_axis=xy[0]
        x_axis=xy[-1]
        print(y_axis,x_axis,arr[y_axis][xy[1]:x_axis+1])
        result+=sum(arr[y_axis][xy[1]:x_axis+1])
        y_axis+=1
    print("정답 : ",result)
