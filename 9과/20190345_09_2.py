N=[x for x in range(1,101)]
M=[];L=[]
for i in range(len(N)) :
    N[i]=int(N[i])
for y in N :
    if y%2==0 :
        M.append(y)
for z in M :
    if z%8==0 :
        L.append(str(z))
print(' '.join(L))

