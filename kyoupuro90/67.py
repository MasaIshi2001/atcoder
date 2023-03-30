
n,k = (int(x) for x in input().split())

nS = str(n)

ansS = nS

ansN = ""

ansT = 0
for i in range(k):

    #change 8 10

    ansT = 0
    
    for i in range(len(ansS)):
        nd = int(ansS[i])
        ansT = ansT*8 + nd

    #change 10 9
    if ansT == 0:
        print(0)
        exit()
    while ansT > 0:
        numN = ansT % 9
        if numN == 8:
            ansN = str(5) + ansN
        else:
            ansN = str(numN) + ansN
        ansT = ansT // 9
    ansS = ansN
    ansN = ""

print(ansS)