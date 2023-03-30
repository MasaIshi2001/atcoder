l,r = (int(x) for x in input().split())
l = l-1
r = r-1
s = str(input())
s = list(s)
while l < r:
    past = s[l]
    s[l] = s[r]
    s[r] = past
    l = l + 1
    r = r - 1

s = "".join(s)
print(s)
