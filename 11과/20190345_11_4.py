print('*'*37)
print('1. 성적 입력(name score1 score2)')
print('2. 학점 부여')
print('3. 출력')
print('4. 프로그램 종료')
print('*'*37)

def M1() :
    L=input("이름 중간 기말 성적을 입력 :").split()
    if len(L)!=3 :
        print("error! 갯수가 맞지 않습니다. 다시 입력해주세요!")
    else :
        X.append(L[0]); Y.append(L[1]); Z.append(L[2])

def M2() :
    for i in range(len(X)) :
        T.append((float(Y[i])*(4/10))+(float(Z[i])*(6/10)))
        if int(T[i])>=90:
            G.insert(i+1,'A')
        elif int(T[i])>=80 :
            G.insert(i+1,'B')
        elif int(T[i])>=70 :
            G.insert(i+1,'C')
        else :
            G.insert(i+1,'D')
    return True

def M3() :
    return True

def M4() :
    print("프로그램을 종료합니다")

X=[]; Y=[]; Z=[]; T=[]; G=[]
k=0
while k==0 or k==2 :
    w=int(input("메뉴 1,2,3,4 번 중 하나 선택 :"))
    if w==1 :
        M1()
        k=0
    elif w==2 :
        if X==[] :
            print("입력된 학생 정보가 없습니다")
        else:
            if M2()==True :
                print("입력된 학생들에게 학점을 부여했습니다.")
        k=2
    elif w==3 :
        if k!=2 :
            print("학점을 부여하지 않은 학생이 있습니다.")
        else :
            if M3()==True :
                print("name   mid    final   grade")
                print('-'*30)
                for i in range(len(X)) :
                    print('%s     %d     %d     %s'%(X[i],int(Y[i]),int(Z[i]),G[i]))
        k=0
    elif w==4 :
        M4()
        k=1
    else :
        print("없는 번호의 명령어입니다. 다시 선택하세요.")
        k=0
        
