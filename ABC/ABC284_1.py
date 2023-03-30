n = int(input())
lis = []
for i in range(n):
    s = str(input())
    lis.append(s)

for i in range(len(lis)):
    print(lis[len(lis)-i-1])