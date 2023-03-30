gyou,retu = (int(x) for x in input().split())

masu_x,masu_y = (int(x) for x in input().split())

ans = 4

if masu_x - 1 == 0:
    ans = ans - 1

if masu_y - 1 == 0:
    ans = ans - 1

if masu_x + 1 > gyou:
    ans = ans - 1

if masu_y + 1 > retu:
    ans = ans - 1

print(ans)