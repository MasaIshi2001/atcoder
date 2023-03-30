nagasa = int(input())
counter = 0
ans_list = []
if nagasa%2 == 0: #長さが偶数の時
    for i in range(2**nagasa):
        if i != 0 or i != 2**nagasa-1:
            bit_line = format(i,'b')
            bit_line = bit_line.zfill(nagasa)
            kakko_line = bit_line.replace('0','(').replace('1',')')
        
            for j in range(nagasa):
                if kakko_line[j] == '(':
                    counter = counter + 1
                elif kakko_line[j] == ')':
                    counter = counter - 1
            
                if counter < 0:
                    break
                if j==nagasa-1 and counter == 0:
                    ans_list.append(kakko_line)
		
            counter = 0
for i in ans_list:
    print(i)


