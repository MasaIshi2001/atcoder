a,b = (int(x) for x in input().split())
if a>0 and b==0:
    print("Gold")
elif a==0 and b>0:
    print("Silver")
else:
    print("Alloy")