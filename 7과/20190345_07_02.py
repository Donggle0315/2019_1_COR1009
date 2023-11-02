L=[1,2,3,4,5]
p=input("리스트 L에 추가할 data를 입력 :")
if p.isnumeric() == True :
    p=float(p)
    if p==L[0] or p==L[1] or p==L[2] or p==L[3] or p==L[4] :
        print("이미 존재하는 데이터입니다.")
        print(L)
    elif p%1==0 :
        p=int(p)
        L[len(L):len(L)]=[p]
        print(L)
    else :
        print("정수 숫자 데이터만 허용합니다.")
        print(L)
else :
    print("정수 숫자 데이터만 허용합니다.")
    print(L)
