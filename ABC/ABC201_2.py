n = int(input())
st_list = []
for i in range(n):
    s,t = (int(x) for x in input().split())
    st_list.append([s,t])

ans = sorted(st_list,key= lambda x: x[1],reverse = True)
print(ans[1])

