x=input("공백으로 구분한 숫자들을 입력 :").split()
y=int(x[0])
for i in range(len(x)) :
    x[i]=int(x[i])
for a in range(len(x)) :
    if y <= x[a] :
        y=y
    else :
        y=x[a]
print("가장 작은 값을 가지는 원소의 인덱스 :", x.index(y))
