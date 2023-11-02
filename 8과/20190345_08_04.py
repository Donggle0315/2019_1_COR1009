fruit={'pear':[2,1000],'apple':[1,2000],'melon':[1,8000],'plum':[6,800]}
x=input("which fruit do you want? :")
if x in fruit :
    print("%s : good taste!"%x)
    y=fruit.get(x)
    z=y[0]-1; w=y[1]
    fruit.update([(x,[z,w])])
else :
    print("%s : sorry, not yet"%x)
L=fruit.items()
L=list(L)
if L[0][1][0] < 5 :
    a=5-L[0][1][0]
    A=a*L[0][1][1]
else :
    A=0
if L[1][1][0] < 5 :
    b=5-L[1][1][0]
    B=b*L[1][1][1]
else :
    B=0
if L[2][1][0] < 5 :
    c=5-L[2][1][0]
    C=c*L[2][1][1]
else :
    C=0
if L[3][1][0] < 5 :
    d=5-L[3][1][0]
    D=d*L[3][1][1]
else :
    D=0
T=A+B+C+D
print()
print("Total charges : %d 원"%T)

