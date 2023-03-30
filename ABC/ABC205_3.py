a,b,c = (int(x) for x in input().split())
if c%2 == 0:
    c = 2
else:
    c = 1

num1 = a**c
num2 = b**c

if num1 > num2:
    print(">")
elif num1 == num2:
    print("=")
else:
    print("<")