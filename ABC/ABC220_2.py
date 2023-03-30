k = int(input())
a,b = (str(x) for x in input().split())

num1 = 0
for i in range(len(a)):
    tmp = int(a[i])
    num1 = 2*num1 + tmp

num2 = 0
for i in range(len(b)):
    tmp = int(b[i])
    num2 = 2*num2 + tmp

print(num1*num2)
