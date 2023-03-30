from collections import deque

n = int(input())
num_lis = [0 for i in range(3*10**5)]
a_list = list(map(int,input().split()))

for i in a_list:
    num_lis[i-1] = 1

a_deq = deque(a_list)

ans_kouho = []
max_renban = 0
not_sakusyo = 0

if a_list[0] == 1:
    not_sakusyo = 1
    max_renban = max_renban + 1
    for i in range(len(a_list)-1):
        if a_list[i+1] - a_list[i] == 1:
            max_renban = max_renban + 1
        else:
            nextpos = i+1
            break
            #暫定の連番最大値

ans_kouho.append(max_renban)#答えの候補に加える
b_flag = False


while len(a_deq) > 1:#長さ1より大きい間
    for i in range(2):#2回削除して
        if a_deq.pop() <= max_renban:
            b_flag = True
    if b_flag == True:
        break
    max_renban = max_renban + 1 #連番を一つ押し上げる
    num_lis[max_renban-1] = 1

    if num_lis[max_renban] == 1:
        max_renban = max_renban + 1

    ans_kouho.append(max_renban)

print(max(ans_kouho))