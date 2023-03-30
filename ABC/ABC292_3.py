n = int(input())

def make_divisors(n):
    cnt = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return cnt 

kouho = []
for i in range(1,n):
    kouho.append([i,n-i])

ans = 0
for i,j in kouho:
    ans += make_divisors(i)*make_divisors(j)

print(ans)



