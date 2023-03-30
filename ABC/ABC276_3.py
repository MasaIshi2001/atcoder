
n = int(input())
p_lis = list(map(int,input().split()))

zouPos = n - 2
while p_lis[zouPos] < p_lis[zouPos + 1]:
    zouPos -= 1 #末尾において単調増加しているところが何処までか調べる

tunaguPos = n - 1
while p_lis[zouPos] < p_lis[tunaguPos]:#単調増加が始まる直前と末尾を比較していって、
    tunaguPos -= 1 #単調増加の末尾内で直前要素以下の最大値を記憶

p_lis[zouPos],p_lis[tunaguPos] = p_lis[tunaguPos],p_lis[zouPos] #入れ替える

print(p_lis[:zouPos-1],p_lis[zouPos-1::-1])



