x, y, z=input("세 개의 정수를 입력하시오 :").split()
x=int(x); y=int(y); z=int(z)
if x<=y<=z :
    [x,y,z]=[x,y,z]
elif x<=z<=y :
    [x,y,z]=[x,z,y]
elif y<=x<=z :
    [x,y,z]=[y,x,z]
elif y<=z<=x :
    [x,y,z]=[y,z,x]
elif z<=x<=y :
    [x,y,z]=[z,x,y]
else :
    [x,y,z]=[z,y,x]
print("내림차순 정렬:", z, y, x)
