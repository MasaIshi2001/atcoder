n =int(input())
s_list = list(map(int,input().split()))

ans_lis = []
past = 0
for i in s_list:
    ans_lis.append(i-past)
    past = i

print(*ans_lis)