n,k = (int(x) for x in input().split())
a_list = list(map(int,input().split()))

amari = k%n
syou = k//n

kokumin = [0 for i in range(n)]

for i in range(n):
    kokumin[i] = syou

for i in range(amari):
    kokumin[i] = kokumin[i] + 1

bangou_lis = sorted(a_list)
bangou = {}
for i in range(len(bangou_lis)):
    bangou[bangou_lis[i]] = i

for i in a_list:
    print(kokumin[bangou[i]])



