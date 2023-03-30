n = int(input())
st_list = []
for i in range(n):
    s,t = (int(x) for x in input().split())
    st_list.append([s,t])

f = len(st_list)
st_set = set(st_list)
s = len(st_set)

if f != s:
    print("Yes")
else:
    print("No")