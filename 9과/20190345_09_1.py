for a in range(10) :
    x=int(input("Enter a number :"))
    if x>0 :
        if x%2==1 :
            print('{} : 양수, 홀수'.format(x))
        else :
            print('{} : 양수, 짝수'.format(x))
    elif x<0 :
        if x%2==1 :
            print('{} : 음수, 홀수'.format(x))
        else :
            print('{} : 음수, 짝수'.format(x))
    else :
        print('입력 받은 수가 {}입니다'.format(x))
        print('프로그램을 종료합니다')
        break
