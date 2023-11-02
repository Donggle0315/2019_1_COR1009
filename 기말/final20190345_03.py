from final20190345_binary import *
import random
L=[]
while len(L)<10 :
    x=random.randint(1,50)
    if x in L :
        continue
    L.append(x)
L=sorted(L)
print("sorted data :", L)

x=int(input("정렬한 리스트에서 찾고자 하는 데이터를 입력 :"))
if x not in L :
    print("%d는 배열에 존재하지 않습니다."%x)
else :
    k=binary_search(x,L)
    print("%d는 배열의 %d번째에 존재합니다"%(x,k))
