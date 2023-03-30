n = int(input())
a_list = list(map(int,input().split()))
x = int(input())

sum1 = 0
sum_lis = []
for i in a_list:
    sum1 = sum1 + i
    sum_lis.append(sum1)

cnt = 0
sum2 = 0

cnt = x//sum1
sa = x%sum1

tmp = 0
i = 0 
while tmp <= sa:
    tmp += a_list[i]
    i += 1


print(cnt*n+i)
