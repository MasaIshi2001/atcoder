n = int(input())
s_line = list(map(int,input().split()))

kouho = []
for i in range(1,144):
    for j in range(1,144):
        kouho.append(4*i*j+3*i+3*j)

cnt = 0

for i in s_line:
    if i not in kouho:
        cnt = cnt + 1

print(cnt)