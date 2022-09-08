num1 = int(input())
num2 = int(input())
a = int(num2/100)
b = int(num2/10)-a*10
c = num2%10
numa = a*num1
numb = b*num1
numc = c*num1
final = numc + numb*10 + numa*100
print(numc)
print(numb)
print(numa)
print(final)

