n,x = (int(x) for x in input().split())

ans_line = ''
for i in range(65,91):
    for j in range(n):
        ans_line = ans_line + chr(i)

print(ans_line[x-1])