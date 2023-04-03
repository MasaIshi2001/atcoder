n = int(input())
s_lis = list(map(int,input().split()))
t_lis = list(map(int,input().split()))

ans_table = [10**9 for j in range(n)]

index_num = t_lis.index(min(t_lis))
ans_table[index_num] = t_lis[index_num]

for i in range(1,n):
    ans_table[(index_num+i)%n] = min(t_lis[(index_num+i)%n],ans_table[(index_num+i-1)%n]+s_lis[(index_num+i-1)%n])

for i in ans_table:
    print(i)

