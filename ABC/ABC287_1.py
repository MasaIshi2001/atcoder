n = int(input())
lis = []
for i in range(n):
    ike = str(input())
    lis.append(ike)

if lis.count("For") > lis.count("Against"):
    print("Yes")
else:
    print("No")