majorB = {"컴퓨터공학" : "AS", "수학" : "R", "전자공학" : "R", "영어영문" : "GA", "심리학":"X"}
x=input("찾는 학과명을 입력 :")
y=majorB.get(x,'Notyet')
if y=='Notyet' :
    print('{}과는 아직 빌딩 정보가 없습니다."GN"건물에 배정합니다.'.format(x))
    majorB.update([(x,'GN')])
else :
    print('{}과는 {}건물에 있습니다.'.format(x,y))
print('**** Building Information ****')
print(majorB)
