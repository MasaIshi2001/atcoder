n = int(input())
nBin = list(bin(n)[2:])
a_list = []
for i in range(len(nBin)):
    if nBin[i] == "1":
        a_list.append(i+1)
 
      
a_list.reverse()
 
 
#まず与えられたnから確実に答えの数が分かる
#与えられたnの2進数表記において1がたっているところ＝自由度2
#0がたっている所＝強制0＝自由度0
#すなわち答えの数は2**(nの二進表記における1の数)
 
ans_lis = []
 
n = 0
for i in range(2**len(a_list)):
    ans = ["0" for i in range(len(nBin))]
    i2 = list(bin(i)[2:]) 
    i2.reverse()
    for j in range(len(i2)):
        if i2[j] == "1":
            ans[a_list[j]-1] = "1"
    ans_line = "".join(ans)
    ans_int = int(ans_line,2)
    ans_lis.append(ans_int)
 
for i in ans_lis:
    print(i)   

