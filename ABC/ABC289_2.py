n,m = (int(x) for x in input().split())
if m == 0:
    ans = [int(x+1) for x in range(n)]
    print(*ans)
    exit()

a_lis = list(map(int,input().split()))
a_lis.append(0)#番兵的なもの追加
ans = [int(x+1) for x in range(n)]#もとの文を作る
renban = False
for i in range(m): 
    if a_lis[i]+1 != a_lis[i+1]: #隣の所にレ点がなかったら
        if renban == False:#そこまでにレ点が連続してなかったら
            ans[a_lis[i]-1:a_lis[i]+1] = [int(x+1) for x in range(a_lis[i],a_lis[i]-2,-1)]#前後をひっくり返す
        else:#レ点が連続してたら
            ans[st-1:fin+1] = [int(x+1) for x in range(fin,st-2,-1)]#まとめてひっくり返したモノと置き換える
            renban = False
    else: #隣の所にレ点があったら
        if renban == False:#開始地点なら
            st = a_lis[i]#開始地点を記憶
        renban = True
        fin = a_lis[i+1]#終了地点を記録
if renban == True:#最後までレ点が続いてたら
    ans[st-1:fin+1] = [int(x+1) for x in range(fin,st-2,-1)]#まとめてひっくり返したモノと置き換える
    renban = False
print(*ans)

