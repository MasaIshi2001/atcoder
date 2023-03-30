n = int(input())

query_set = set()
ans_set = []

for i in range(n):
    name = str(input())
    if name not in query_set:
        query_set.add(name)
        ans_set.append(i+1)

for i in ans_set:
    print(i)
