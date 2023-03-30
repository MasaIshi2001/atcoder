syoki,limit,multi = (int(x) for x in input().split())

count = 0
while syoki < limit:
    syoki *= multi
    count = count + 1

print(count)