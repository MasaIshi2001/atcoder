import bisect

n = int(input())
a_lis = list(map(int,input().split()))

a_set = set(a_lis)
a_lis2 = list(a_set)
a_lisS = sorted(a_lis2)
kouho_lis = []

for i in a_lis:
    pos = bisect.bisect(a_lisS,i)
    kouho_lis.append(len(a_set)-pos)

ans_lis = [0 for i in range(n+1)]
kouho_lis.sort()
for i in kouho_lis:
    ans_lis[i] = ans_lis[i] + 1

for i in ans_lis:
    print(i)


    