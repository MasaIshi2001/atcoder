n = int(input())
c_lis = list(map(int,input().split()))

c_lis.sort()

ans = 1
kaburi = 0

for i in c_lis:
    if i-kaburi > 0:
        ans *= i-kaburi
        ans = ans % ((10**9+7))
        kaburi += 1
    else:
        print(0)
        exit() 

print(ans%((10**9+7)))