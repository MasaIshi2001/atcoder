n = int(input())
a_lis = list(map(int,input().split()))

dicti = {}
for i in range(n):
    if i+1 not in dicti:
        dicti[i+1] = a_lis[i]

for i,v in dicti.items():
    