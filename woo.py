pen = {'red' : 300, 'green' : 400, 'blue' : 2000 }
a = input()
if(a == 'all'):
    s = sorted(pen.items(), key = lambda x : x[1], reverse =True)
    # lambda 매개변수 : 리턴값 ->  lambda x :x[1] 은 x[1]을 key값으로 생각하겠다는 뜻
    # 원래는 x[0]가 key값. sorted(딕셔너리이름.items()) -> key값을 기준으로 오름차순으로 정렬
    print(s)
elif (a=='red'):
    print(pen['red'])
elif (a=='green'):
    print(pen['green'])
elif (a=='blue'):
    print(pen['blue'])
elif (a=='end'):
    exit()


