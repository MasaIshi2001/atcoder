n = int(input())
x_lis = list(map(int,input().split()))

x_lis.sort()
print(sum(x_lis[n:5*n-n])/(3*n))