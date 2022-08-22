def calcu(wd,dd):
    # wd is word, dd is difference word
    if wd==dd:
        return 0
    else:
        cnt=0
        result=0
        for i in wd:
            if i!=dd[cnt]:
                result+=1
        return result
    
sentence=input()
word_count=int(input())
word=[input() for i in range(word_count)]
start=0;Flag=True

while start!=len(sentence)-1: #문장의 끝까지 도달
    for i in word: # 단어 순회
        for j in i: # 문장 단어 검사
            if j not in sentence[start:len(i)]: # 매칭여부 확인
                Flag=False
                break
        if Flag==True:
            start+=len(i)-1
            result=calcu(word,i)
    if start!=len(sentence)-1:
        print(-1)        
print(result)