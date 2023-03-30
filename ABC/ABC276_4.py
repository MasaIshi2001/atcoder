import math
n = int(input())
a_list = list(map(int,input().split()))

#解説　最大公約数の利用を考える
#      まず全ての要素は a = 2**i + 3**j + z(2でも3の倍数でもない数) で表現可能 
#      2で割る操作はiを減らし、3で割る操作はjを減らすということとなる
#      ここで目的の合わせる数というのはリストの中の最小の値である
#　　　この最小の値とは a = 2**i + 3**j + zの i と j が最小のものである
#      すなわち要素間の最大公約数を用いれば合わせられるかどうかとこの合わせるべき最小の数が分かる

#step1 要素の最大公約数を求める
g = 1
for i in range(n):
    g = math.gcd(g,a_list[i])

#step2 要素をそれぞれ最大公約数で割り、本来合わせるべき数の分要素を除いておく
#      2と3で割る操作を行なっていく
# 　　 要素が1となればOK,要素が1にならなかったら合わせることは不可能ということになる

ans = 0
for i in range(n):
    a_list[i] /= g
    while a_list[i]%2 == 0:
        a_list[i] /= 2
        ans = ans + 1
    while a_list[i]%3 == 0:
        a_list[i] /= 3
        ans = ans + 1
    if a_list[i] != 1:
        print(-1)
        exit()

print(ans)    


