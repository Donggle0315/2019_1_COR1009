x=input("문자열 입력 :")
def include() :
    x.replace(" ",""); x.lower()
    D=dict()
    for i in range(len(x)) :
        D.update(x[i])
    print(D)
print(include())
