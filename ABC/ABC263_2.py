n = int(input())
p_lis = list(map(int,input().split()))

dicti = {}
cnt = 2
for i in p_lis:
    dicti[cnt] = i
    cnt = cnt + 1

daime = n
nanndai = 0

while daime != 1:
    oya = dicti[daime]
    daime = oya
    nanndai = nanndai + 1

print(nanndai)