import numpy as np
import math
 
def solve(m):#この関数は長さを二つに分けてどっちに答えが所属しているか判別する
    cnt = 0 #カウント用変数
    pre = 0 #一旦切った位置を保存するための変数
    for i in range(kireme):                                           #切れ目が入れられている位置を片っ端から試す
        if(kireme_lis[i] - pre >= m and nagasa - kireme_lis[i] >= m): #長さm以上のピースに切れ目で区切れると分かったら
            cnt = cnt + 1                                             #分けた回数としてカウントして
            pre = kireme_lis[i]                                       #一旦その切れ目で切る    
    
    if cnt >= choice_num: #choice_num+1以上に分かれる場合
        return True       #下限を動かす
    else:                 #分かれない時
        return False      #上限を動かす
 
#step1 入力
kireme,nagasa = (int(x) for x in input().split())
choice_num = int(input())
kireme_lis = list(map(int,input().split()))
 
#step2 二分探索
#２分探索木によって解く。答えは0以上nagasa以下と分かっている。この範囲内で答えが M 以上かどうか調べていって答えを導く
#方法はchoice_num＋１個以上の長さM以上のピースに分けられるか判定していく
 
left = 0                           #下限を0とする
right = nagasa                     #上限を長さとする
while right - left  > 1:           #上限と下限との差が１より大きい間
    mid = left + (right - left)/2  # 長さの中央値を求める
    mid = math.floor(mid)          # 中央値を丸める
    if solve(mid) == False:        #choice_num＋１個以上の長さM以上のピースに分けられない場合
        right = mid                #答え範囲の上限を動かす
    else:                          #choice_num＋１個以上の長さM以上のピースに分けられる場合
        left = mid                 #答え範囲の下限を動かす
 
print(left)

#上のような最小値の中の最大値の探索には二分探索手法が有効なことが多い