n,x,y,z = (int(x) for x in input().split())
suugaku_list = list(map(int,input().split()))
eigo_list = list(map(int,input().split()))
 
flag = [0]*n              #合格者リストを作っておいて合格者がいる場所には1が立つようにする
for i in range(x):        #数学によって最初に出される合格者を出す
    pos = -1              #合格者位置の初期化
    for j in range(n):    #受験者の総当たり戦開始
        if flag[j] != 1:  #既に合格が出ていないかチェック。合格が出ていないやつは以下の処理
            if pos == -1 or suugaku_list[j]>suugaku_list[pos]:  #最初のやつor暫定優秀なやつより優秀なやつは以下の処理
                pos = j   #最初のやつor暫定優秀なやつより優秀なやつの場所を記憶
    flag[pos] = 1         #posには総当たり戦の結果既に合格していない奴らの中で最優秀なやつの番号を示すので、そこに合格フラグを立てる
 
for i in range(y):        #英語によって出される合格者を出す
    pos = -1              #合格者位置の初期化
    for j in range(n):    #受験者の総当たり戦開始
        if flag[j] != 1:  #既に合格が出ていないかチェック。合格が出ていないやつは以下の処理
            if pos == -1 or eigo_list[j]>eigo_list[pos]:   #最初のやつor暫定優秀なやつより優秀なやつは以下の処理
                pos = j   #最初のやつor暫定優秀なやつより優秀なやつの場所を記憶
    flag[pos] = 1         #posには総当たり戦の結果既に合格していない奴らの中で最優秀なやつの番号を示すので、そこに合格フラグを立てる
 
for i in range(z):        #合計点によって出される合格者を出す
    pos = -1              #合格者位置の初期化
    for j in range(n):    #受験者の総当たり戦開始
        if flag[j] != 1:  #既に合格が出ていないかチェック。合格が出ていないやつは以下の処理
            if pos == -1 or suugaku_list[j] + eigo_list[j]>suugaku_list[pos] + eigo_list[pos]:  #最初のやつor暫定優秀なやつより優秀なやつは以下の処理
                pos = j   #最初のやつor暫定優秀なやつより優秀なやつの場所を記憶
    flag[pos] = 1         #posには総当たり戦の結果既に合格していない奴らの中で最優秀なやつの番号を示すので、そこに合格フラグを立てる
 
for i in range(n):
    if flag[i] == 1:     #合格フラグが立っていたら
        print(i+1)       #そいつの受験番号を出力