from collections import defaultdict

n = int(input())
num_lis = list(map(int,input().split()))

tmp = 0
tmp_dic = defaultdict(int)
for i in num_lis:
    if tmp_dic[i] == 0:
        tmp_dic[i] == 1
        tmp += 1
    else:
        tmp_dic[i] == 0

print(len(num_lis) - tmp)

    

