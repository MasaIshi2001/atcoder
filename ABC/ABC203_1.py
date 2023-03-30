a,b,c = (int(x) for x in input().split())
lis= [a,b,c]
sum = a+b+c
for i in range(len(lis)-1):
    for j in range(i+1,len(lis)):
        if lis[i] == lis[j]:
            print(sum - (lis[i]*2))
            exit()

print(0)



