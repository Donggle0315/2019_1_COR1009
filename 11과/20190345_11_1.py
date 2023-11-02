def password(x) :
    y=0
    for i in range(10) :
        z=x.count(str(i))
        y=y+z
    if x.isalpha()==True or x.isnumeric()==True :
        print("error! 영문 또는 숫자로만 구성되면 안됨")
        return False
    elif x.isalnum()==False :
        print("error! 영문자, 숫자로만 구성되어야 함")
        return False
    elif len(x)<8 :
        print("error! 8 글자 이상이어야 함")
        return False
    elif y<2 :
        print("error! 최소한 2개의 숫자를 포함해야 함")
        return False
    else :
        return True

i=0        
while i <6 :
    x=input("Enter password:")
    if password(x)==True :
        print("Valid password")
        break
    else :
        print("Invalid password")
        i=i+1
