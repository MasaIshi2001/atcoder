n = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

#hit count
hit_count = 0
for i in range(len(a_list)):
    if a_list[i] == b_list[i]:
        hit_count = hit_count + 1

#blow count
blow_count = 0
for i in range(len(a_list)):
    for j in range(len(b_list)):
        if  i != j:
            if a_list[i] == b_list[j]:
                blow_count = blow_count + 1

print(hit_count)
print(blow_count)

#約7分で解決(自分)