a,b = (int(x) for x in input().split())
if b-a < 0:
    print(0)
    exit()

print(b-a+1)