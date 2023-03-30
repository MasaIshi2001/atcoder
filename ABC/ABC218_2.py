p_line = list(map(int,input().split()))
ch_list = [chr(ord("a")+i) for i in range(26)]

ans = ""
for i in p_line:
    ans = ans + ch_list[i-1]

print(ans)