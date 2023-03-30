n,y = (int(x) for x in input().split())
osatulis = [10000,5000,1000]
kouho = [-1,-1,-1]
pos = 0

for i in range(n+1):
    for j in range(n+1):
        z = n - i - j
        if 0 <= z:
            if i*osatulis[0] + j*osatulis[1] + z*osatulis[2] == y:
                kouho = [i,j,z]
                for i in kouho:
                    print(i)
                    exit()

for i in kouho:
    print(i)











