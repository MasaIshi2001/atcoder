
n = int(input())
a_list = list(map,int,input().split())

sumNum = 0 
num1 = 0

for i in a_list:
    num1 += i**2

sumNum = n*num1 - sum(a_list)**2
print(sumNum)