x=input("대출금 입력 : ")
y=input("년 이자율 입력(%단위) : ")
x=int(x); y=float(y)
print("매달 지급해야할 이자는 {} 입니다".format(int(x*(y/100)/12)))
