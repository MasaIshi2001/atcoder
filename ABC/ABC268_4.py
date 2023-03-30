import itertools


n,m = (int(x) for x in input().split())
s_list = []
for i in range(n):
    s = input()
    s_list.append(s)

t_list = []
for i in range(m):
    t = input()
    t_list.append(t)

conb_lis = list(itertools.permutations(s_list,n))

