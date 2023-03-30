a,b = (int(x) for x in input().split())
if abs(a-b) == 1:
    print("Yes")
elif a==1 and b== 10:
    print("Yes")
elif a==10 and b== 1:
    print("Yes")
else:
    print("No")