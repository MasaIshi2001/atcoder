n,k =(int(x) for x in input().split())
a_list = list(map(int,input().split()))

for i in range(k):
    for j in range(n):
        if j == n-1:
            a_list[j] = 0
        else:
            a_list[j] = a_list[j+1]

print(*a_list)
