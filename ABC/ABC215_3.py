import itertools 

s,k =(str(x) for x in input().split())
k = int(k)
s = list(s)

pre_ans = list(itertools.permutations(s))
ans = list(set(pre_ans))
ans.sort()
print("".join(ans[k-1]))

