N=int(input("Enter # of lines :"))
if N%2==1 and N>=1 :
    for i in range(int((N+1)/2)) :
        for j in range(i) :
            print("*", end="")
        print()
    for i in range(int((N+1)/2),0,-1) :
        for j in range(i) :
            print("*",end="")
        print()
else :
    print("N must be >=1 and odd!")
