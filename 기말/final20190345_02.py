def function1(L) :
    for i in range(len(L)) :
        D[L[i]]=D.get(L[i],0)+1
    k=len(D)
    return D,k

def function2(D) :
    P=list(D.values())
    O=list(D.keys())
    for i in range(len(P)-1) :
        for j in range(len(P)-i-1) :
            if P[j] > P[j+1] :
                q=P[j]
                P[j]=P[j+1]
                P[j+1]=q
                w=O[j]
                O[j]=O[j+1]
                O[j+1]=w
                P.reverse(); O.reverse()
    return P,O



import random
L=[]; D=dict()
for i in range(10) :
    L.append(random.randint(1,20))
D,k=function1(L)
print(L)
print(D)
print('*'*47)
print("사용된 숫자의 수 : %d"%k)
print()
print("숫자별 출현횟수(내림차순)")
P,O=function2(D)
for i in range(len(P)) :
    print("%2d       %2d"%(O[i],P[i]))
