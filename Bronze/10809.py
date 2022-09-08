word = input()
#아스키코드 소문자 a~z = 97~122
list1 = [-1 for _ in range (26)]
for i in range (len(word)):
    # 모든 글자에서 - 97을 하면 그 위치가 나옴
    b= ord(word[i])-ord('a') #ord는 아스키코드로 바꿔주는 것
    if(list1[b] == -1):
        list1[b] = i
for i in range (26):
    print(list1[i],end =' ')