n,k = (str(x) for x in input().split())
k = int(k)
n= list(n)

for i in range(k):
    n1 = sorted(n)
    n2 = sorted(n,reverse=True)
    n = n2 -n1

print(n)