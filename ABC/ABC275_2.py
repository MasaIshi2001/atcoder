a,b,c,d,e,f = (int(x) for x in input().split())
ans = (a*b*c)-(d*e*f)
print(ans%998244353)