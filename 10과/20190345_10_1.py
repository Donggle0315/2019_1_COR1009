L=list()
a=0
while a==0 :
    x=input("정수를 입력 (0을 입력하면 종료) :")
    if x=='' or x=='0' :
        a=1
    else :
        x=int(x)
        L.append(x)
if L==[] :
    y=0; z=0; w=0
else :
    y=sum(L); z=len(L); w=y/z

print("입력한 정수 리스트 :",L)
print("합계 :",y)
print("평균 :",w)
