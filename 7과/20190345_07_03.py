a=input("첫번째 문자열의 입력:")
b=input("두번째 문자열의 입력:")
A=sorted(list(a)); B=sorted(list(b))
if A==B :
    print("{}, {} 는 anagram입니다.".format(a,b))
else :
    print("{}, {} 는 anagram이 아닙니다.".format(a,b))
