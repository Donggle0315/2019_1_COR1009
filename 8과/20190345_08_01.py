employee={'공유','고수','보검','태현','종민','세윤','준호','우종','시우','두준'}
late={'우종','보검'}
absent={'종민','우종','보검','두준'}
A=late|absent; B=employee-A; C=late&absent
print("전체 사원 명단 :", employee)
print("지각자 명단 :", late)
print("결근자 명단 :", absent)
print("보너스 지급 대상자 명단 :", B)
print("야근 대상자 명단 :", C)
E=set(input("신입사원 명단 입력 :").split())
if E.isdisjoint(employee) != True :
    D=E.intersection(employee)
    print("신입사원 {}은 기존 사원의 이름과 같음".format(D))
F=employee|E
print('전체 사원 명단 :', F)
