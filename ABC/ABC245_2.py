n = int(input())
a_list = []
a_list = list(map(int,input().split()))

for i in range(2000):
    if i not in a_list:
        ans_num = i
        break

print(ans_num)
