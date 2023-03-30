import itertools

n,m = (int(x) for x in input().split())

for x in itertools.combinations(range(1,m+1),n):
    print(*x)
    
