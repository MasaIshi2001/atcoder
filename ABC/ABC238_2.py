n = int(input())
a_list = list(map(int,input().split()))

kaku_list = [0]*360
kaku_list[360] = 1
kaku_list[0] = 1
kaku_sum = 0

for i in a_list:
    kaku_sum += i
    kirikomi = kaku_sum % 360
    kaku_list[kirikomi] = 1

res_lis = []
past_i = 0

for i in range(len(kaku_list)):
    if kaku_list[i] == 1:
        res_lis.append(i-past_i)
        past_i = i

print(max(res_lis))
