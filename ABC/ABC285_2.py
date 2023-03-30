n = int(input())
s = input()

for i in range(n-1):
    j = i+1
    f = 0
    p = 0
    pos = 0
    cnt = 0
    f =  pos + j
    while f <= len(s):
        if s[pos] == s[f]:
            break
        cnt += 1
        pos += 1
        f =  pos + j

    print(cnt)
