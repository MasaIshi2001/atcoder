import itertools
n = []
n = list(str(input()))
 
kouho = list(itertools.permutations(n))
ans = -1
for i in kouho:
    i = list(i)
    for s in range(len(i)):
        i[s] = str(i[s])
 
    for j in range(len(i)-1):
        a = int("".join(i[:j+1]))
        b = int("".join(i[j+1:]))
        ans = max(a*b,ans)
 
print(ans)