import random

def dice() :
    l=0
    global q
    for i in range(1,x+1) :
        p=int(l/i*100)
        if i <=10 :
            k=random.randint(0,2)
            if k==1 :
                l=l+1
            print("{}번째까지 던지기에서 앞면이 나온 확률 : {}%".format(i,p))
        else :
            k=random.randint(0,2)
            if k==1 :
                l=l+1
            if i%10==0 :
                print("{}번째까지 던지기에서 앞면이 나온 확률 : {}%".format(i,p))
        q=p

                
x=int(input("동전 던지기 시도 횟수를 입력(1-100) :"))
dice()
print("******************************************************************")
print("총 {}번 동전 던지기에서 앞면이 나올 확률 : {}%".format(x,q))
