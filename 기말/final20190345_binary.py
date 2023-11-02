def binary_search(x,L) :
    T=L[:]
    while True :
        p=len(L)
        if L.index(x)<int(p/2):
            L=L[:int(p/2)]
        elif L.index(x)>int(p/2) :
            L=L[int(p/2)+1:]
        else :
            L=L[int(p/2)]
        if L==x :
            return T.index(L)+1
            break
