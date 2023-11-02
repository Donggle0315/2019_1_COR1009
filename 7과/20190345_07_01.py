L=[[1,3,5],[7,9],[],[11]]
a=L[0]; b=L[1]; c=L[2]; d=L[3]
a1,a2,a3=a[0],a[1],a[2]
b1,b2=b[0],b[1]
d1=d[0]
A=(a1**2)+(a2**2)+(a3**2)
B=(b1**2)+(b2**2)
D=d1**2
DL=[A,B,D]
DL.sort(reverse=True)
print('DoubleL =',DL)
