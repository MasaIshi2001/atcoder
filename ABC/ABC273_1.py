def r(n):
    if r > 0:
        return r*r(n-1)
    else:
        return 1


n = int(input())
ans = r(n)
print(ans)