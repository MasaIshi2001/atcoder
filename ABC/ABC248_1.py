num_str = str(input())
sum_1 = 0

for i in range(len(num_str)):
    sum_1 += int(num_str[i])

sum_2 = sum([0,1,2,3,4,5,6,7,8,9])

print(sum_2 - sum_1)
