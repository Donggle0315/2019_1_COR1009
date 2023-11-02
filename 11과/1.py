x=input("Enter password :")
def password(x) :
    if len(x) < 8 :
        return"error! 8 글자 이상되어야 함"
    if x.isnumeric()==True :
        return "error! 영문도 포함되어야 함"
    if x.isalpha()==True :
        return "error! 숫자도 포함되어야 함"
    if x.isalnum()==False :
        return "error! 영문자, 숫자로만 구성되어야 함"
    
    k=0
    for i in range(10):
        y=x.count(i)
        k=k+y
    if k<2 :
        return "error! 최소한 2개의 숫자를 포함해야 함"
    else :
        return "Valid password"
print(password(x))
