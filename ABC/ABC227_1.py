n,k,a = (int(x) for x in input().split())

nokori = k - a
if k%n != 0:
    print(k%n)
else:
    print(n)