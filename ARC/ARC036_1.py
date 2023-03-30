
n,k = (int(x) for x in input().split())
t_lis =[]
for i in range(n):
    t = int(input())
    t_lis.append(t)
days = 3
for i in range(2,n):
    if t_lis[i] + t_lis[i-1] + t_lis[i-2] < k:
        print(days)
        exit()
    days = days + 1

print(-1)
