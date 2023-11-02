x=int(input("구하려는 소수의 개수를 입력 :"))
L=list()
if x<=0 :
    print("^^")
else :
    L.append(2)
    a=2
    while len(L)<=x :
        A=True
        for i in range(2,a):
                if a % i == 0 :
                    A=False
                    break
                else :
                    A=True
        if A==True :
            L.append(a)
            print(a)
        a=a+1
    print("%d 개의 소수를 찾았습니다"%(len(L)-1))
            

