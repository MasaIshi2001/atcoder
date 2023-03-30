a,b = (int(x) for x in input().split())
if 15 <= a and 8 <= b:
    print(1)
elif 10 <= a and 3 <= b:
    print(2)
elif 3 <= b:
    print(3)
else:
    print(4)