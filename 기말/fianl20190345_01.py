x=input("문장 입력 :"); L=[]
while True :
    y=input("입력 받은 문장에서 단어를 제외한 제거할 문자 하나 입력 :")
    if y=='' :
        break
    x=x.replace(y,'')
    print(x)
L=list(sorted(set(x.split())))
print("중복 제거한 단어 리스트 :", L)
