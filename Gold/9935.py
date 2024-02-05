string = list(input())
bomb = list(input())
stack = []
for i in range(len(string)):
    stack.append(string[i])
    if len(stack) < len(bomb):
        continue
    if stack[len(stack)-len(bomb):] == bomb:
        del stack[len(stack)-len(bomb):]

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))

# 11% 시간초과
# def remove_bomb(string):
#     l = len(bomb)
#     for i in range(len(string)):
#         if len(string) < len(bomb):
#             break
#         else:
#             if string[i:i+l] == bomb:
#                 string = string[:i] + string[i+l:]
#     return(string)

# while True:
#     if bomb in string:
#         string = remove_bomb(string) 
#     else:
#         break  

# if len(string) == 0:
#     print('FRULA')
# else:
#     print(string)

# 46% 시간초과
# while True:
#     if bomb in string:
#         string = string.replace(bomb,'')
#     else:
#         break  

# if len(string) == 0:
#     print('FRULA')
# else:
#     print(string)

