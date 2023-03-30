x,y = (int(x) for x in input().split())
cnt = 0
while x < y:
    x = x + 10
    cnt = cnt + 1

print(cnt)