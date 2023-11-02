y,z,w=input("수식 입력(예: 20 * 40) :").split()
y=float(y); w=float(w)
if z == '+' :
    print("{:.6f} + {:.6f} = {:.6f}".format(y,w,y+w))
elif z =='-' :
    print("{:.6f} - {:.6f} = {:.6f}".format(y,w,y-w))
elif z =='*' :
    print("{:.6f} * {:.6f} = {:.6f}".format(y,w,y*w))
elif z =='/' :
    if w==0 :
        print("{:.6f} 로 나누기를 수행할 수 없습니다.".format(w))
    else :
        print("{:.6f} / {:.6f} = {:.6f}".format(y,w,y/w))
else :
    print("{} 지원하지 않는 연산자입니다.".format(z))
