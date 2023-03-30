n = int(input())
a_list = list(map(int,input().split()))

syu = 0
for i in a_list:
    if i > 10:
        syu += i - 10
print(syu)
