def f(x) :
    x=x.lower()
    x=x.replace(" ","")
    d=dict()
    k=1
    for i in range(len(x)) :
        k=1
        for j in range(i) :
            if x[i]==x[j] :
                k=k+1
            else :
                k=k
            d[x[i]]=k
    a=list(d.keys())
    b=list(d.values())
    for i in range(len(d)) :
        print(a[i],':', b[i])
                
        

x=input("문자열 입력 :")
f(x)
