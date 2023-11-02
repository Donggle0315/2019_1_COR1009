x=input("랜덤하게 원하는 횟수만큼 입력(1에서 10사이):").split()
for i in range(len(x)) :
    x[i]=int(x[i])
    t=1
while t<=10 :
    print('숫자 %d는 %d번 입력 되었습니다.'%(t,x.count(t)))
    t=t+1
