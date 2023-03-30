s = str(input())
a,b = (int(x) for x in input().split())
sL = list(s)
past = sL[a-1]
sL[a-1] = sL[b-1]
sL[b-1] = past
ans = "".join(sL)
print(ans)