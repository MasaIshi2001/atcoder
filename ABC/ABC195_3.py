import decimal
d = decimal.Decimal(input())

ans = 0

if d >= 10**3:
    ans = d - 999

if d >= 10**6:
    ans += d - (10**6 - 1)

if d >= 10**9:
    ans += d - (10**9 - 1)

if d >= 10**12:
    ans += d - (10**12 - 1)

if d >= 10**15:
    ans += d - (10**15 - 1)

print(ans)