a,b,c=input("세 변의 길이를 입력 :").split()
a=float(a); b=float(b); c=float(c)
if a>=b and a>=c :
    [a,b,c]=[a,b,c]
elif b>=a and b>=c :
    [a,b,c]=[b,a,c]
elif c>=a and c>=b :
    [a,b,c]=[c,a,b]
print(a,b,c)
if a>=b+c :
    print("삼각형이 아님")
elif a==b!=c or a==c!=b or b==c!=a :
    print("이등변 삼각형임")
elif a==b==c :
    print("정 삼각형임")
elif (a**2)==(b**2)+(c**2) :
    print("직각 삼각형임")
else :
    print("일반 삼각형임")
    
