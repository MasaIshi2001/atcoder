import math

k = int(input())
rem = k

ans_lis = []
roop = int(math.sqrt(k))
for i in range(1,roop):
    while rem%(i+1)==0:
        rem = rem//(i+1)
        ans_lis.append(i)
ans_lis.append(rem)
ans_dic = {}
for i in ans_lis:
    if i not in ans_dic.keys():
        ans_dic[i] = 0
    ans_dic[i] = ans_dic[i] + 1


print(max(ans_lis))

