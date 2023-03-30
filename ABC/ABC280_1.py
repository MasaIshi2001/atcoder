h,w =(int(x) for x in input().split())
s_list = []
for i in range(h):
    s = str(input())
    s_list.append(s)

ans = 0
for i in s_list:
    ans = ans + i.count("#")
print(ans)
