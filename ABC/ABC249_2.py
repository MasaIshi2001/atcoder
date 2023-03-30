s = input()

s_list = list(s)
s_list = sorted(s_list)

low_count = 0
up_count = 0
same_count = 0
past_char = ''

for i in s_list:
    i = str(i)
    if i.islower() == True:
        low_count += 1
    
    if i.isupper() == True:
        up_count += 1
    
    if past_char == i:
        same_count = 1

    past_char = i

if low_count >= 1 and up_count >= 1 and same_count == 0:
    print("Yes")
else:
    print("No")