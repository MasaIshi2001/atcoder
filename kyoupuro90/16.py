n = int(input())
a,b,c = (int(x) for x in input().split())
max_maisuu = 9999

for i in range(10000):
    for j in range(10000-i):
        z = n - a*i -b*j
        if z%c != 0 or z < 0 or i + j + z%c > 9999:
            continue
        
        maisuu = i + j + z/c
        max_maisuu = min(max_maisuu,maisuu)
        
print(int(max_maisuu))