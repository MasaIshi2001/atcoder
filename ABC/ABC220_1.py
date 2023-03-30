a,b,c = (int(x) for x in input().split())

for i in range(a,b+1):
    if i%c == 0:
        print(i)
        exit()
        
print(-1)