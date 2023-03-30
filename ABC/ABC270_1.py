a,b = (int(x) for x in input().split())
if a==b:
    print(a)
    exit()

a = bin(a)
b = bin(b)
print(a|b)