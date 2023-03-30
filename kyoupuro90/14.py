n = int(input())
ie_lis = list(map(int,input().split()))
ga_lis = list(map(int,input().split()))

ie_lis.sort()
ga_lis.sort()
dis = 0

for i in range(n):
    dis += abs(ie_lis[i] - ga_lis[i])

print(dis)