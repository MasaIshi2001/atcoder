n = int(input())
A_query_list = list(map(int,input().split()))

p = 0

koma_position = [0]*5


count_pos = 1

for i in A_query_list:
    
    for k in range(count_pos):
        koma_position[k] += i
        
        if koma_position[k] >= 4:
            p = p + 1
            koma_position[k] = 0
            count_pos = count_pos - 1
        
        
    list.sort(koma_position,reverse=True)
    count_pos = count_pos + 1

print(p)