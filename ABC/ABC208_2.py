p = int(input())
tmp_lis = [1,2,3,4,5,6,7,8,9,10]
k_lis = []
for i in tmp_lis:
    num = 1
    for j in range(i):
        num = num*j
    k_lis.append(num)

k_lis.reverse()
cnt = 0
pos = 0
for i in range(k_lis):
    if p > i:
        pos = i
        break

while p > 0:
    cnt += p//k_lis[pos]
    p = p % k_lis[pos]
    pos = pos + 1

print(cnt)