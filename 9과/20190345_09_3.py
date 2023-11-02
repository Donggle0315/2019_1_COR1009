A=[4,8,2,3,4,2]
B=[7,2,5,2,3,6,5]
C=[]
D=[]
for a in range(len(A)) :
    for b in range(len(B)) :
        if A[a]==B[b] :
            C.append(A[a])
C.sort()
for i in range(len(C)) :
    if C[i] not in D :
        D.append(C[i])
D.sort()
print(D)
            
