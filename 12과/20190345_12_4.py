def BS(x) :
    for i in range(0,len(L)-1):
        for j in range(0,len(L)-i-1) :
            if L[j]>L[j+1] :
                p=L[j]
                L[j]=L[j+1]
                L[j+1]=p
    return L
    

import random
L=[]
while len(L)<10 :
    k=random.randint(1,51)
    L.append(k)
print("Before bubble sort :",L)
L=BS(L)
print("After bubble sort :",L)
x=int(input("정렬한 리스트에서 찾고자 하는 데이터를 입력 :"))
if x in L :
    print("%d는 배열의 %d번째에 존재합니다"%(x,L.index(x)+1))
else :
    print("%d는 배열에 존재하지 않습니다"%x)
