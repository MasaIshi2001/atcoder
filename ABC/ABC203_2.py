n,k = (int(x) for x in input().split())
sum = 0
for i in range(n):
    for j in range(k):
        num = (i+1)*100 + (j+1)
        sum += num

print(sum)
