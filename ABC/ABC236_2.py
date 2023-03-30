n = int(input())
a_list = list(map(int,input().split()))
isum = 0
for i in range(n+1):
    isum += i

isum2 = 4*isum
afsum = sum(a_list)
print(isum2-afsum)