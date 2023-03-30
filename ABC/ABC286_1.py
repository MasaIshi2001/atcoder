n,p,q,r,s = (int(x) for x in input().split())
a_lis = list(map(int,input().split()))

tmp =[]
tmp = a_lis[p-1,q]
a_lis[p-1,q] = a_lis[r-1,s]
a_lis[r-1,s] = tmp

print(*a_lis)
