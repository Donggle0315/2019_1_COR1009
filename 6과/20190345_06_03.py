x,y=input("두 자리 정수 두개를 입력 :").split()
x1=x[0]; x2=x[1]; y1=y[0]; y2=y[1]
if x1==y1 and x2==y2 :
    print("두 정수는 모두 {}로 같은 정수입니다.".format(x))
elif x1==y2 and x2==y1 :
    print("{}, {}: 자리 값만 다른 정수입니다.".format(x,y))
elif x1==y1 or x1==y2 or x2==y1 or x2==y2 :
    print("{}, {} : 하나의 숫자만 일치합니다.".format(x,y))
else :
    print("{}, {} : 일치하지 않는 정수입니다.".format(x,y))
