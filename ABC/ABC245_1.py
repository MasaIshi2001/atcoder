a,b,c,d = (int(x) for x in input().split())

if a < c:
    print("Aoki")
elif a > c:
    print("Takahashi")
else:
    if b < d:
        print("Aoki")
    else:
        print("Takahashi")