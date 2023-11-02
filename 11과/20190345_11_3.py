def HimDleDa(x) :
    BIG=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    SMALL=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(x)) :
        if x[i] in BIG :
            y=BIG.index(x[i])
            x=x[:i]+SMALL[y]+x[i+1:]
        elif x[i] in SMALL :
            y=SMALL.index(x[i])
            x=x[:i]+BIG[y]+x[i+1:]
    return print(x)

x=input("Enter sting :")
HimDleDa(x)
