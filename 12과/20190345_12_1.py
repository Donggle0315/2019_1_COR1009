def plus(a,b) :
    c=a+b
    return c
def minus(a,b) :
    c=a-b
    return c
def multi(a,b) :
    c=a*b
    return c
def div(a,b) :
    c=a/b
    return c


x=input("수식 입력(예: 20*40) :").split()
x[0]=float(x[0]); x[2]=float(x[2]) 
if x[1]=='+' :
    print("{:.6f} + {:.6f} = {:.6f}".format(x[0],x[2],plus(x[0],x[2])))
elif x[1]=='-' :
    print("{:.6f} - {:.6f} = {:.6f}".format(x[0],x[2],minus(x[0],x[2])))
elif x[1]=='*' :
    print("{:.6f} * {:.6f} = {:.6f}".format(x[0],x[2],multi(x[0],x[2])))
elif x[1]=='/' :
    if x[2]==0 :
        print("{:.6f}로 나누기를 수행할 수 없습니다".format(x[2]))
    else:
        print("{:.6f} / {:.6f} = {:.6f}".format(x[0],x[2],div(x[0],x[2])))
else :
    print("{} 지원하지 않는 연산자입니다".format(x[1]))
