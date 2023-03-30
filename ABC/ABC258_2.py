
n = int(input())
A_list = []
for i in range(n):
    A_line = str(input())
    temp_list = list(A_line)
    A_list.append(temp_list)

ans = 0

#以下の2つのリストの動きを組み合わせて8方向の全探索を行なう

x_move_list = [1,1,1,0,0,-1,-1,-1] #x方向の動き
y_move_list = [1,0,-1,1,-1,1,0,-1] #y方向の動き

#以下の処理で探索を行なう

for i in range(n):  #x座標のi
    for j in range(n): #y座標のj
        for k in range(8): #方向を選択するk
            now = 0 #一時的に数字を補完しておく変数
            x = i   #x座標
            y = j   #y座標
            
            for l in range(n):
                now *= 10  #桁送り
                now += int(A_list[y][x]) #現在のマスの数字の取得
                x += x_move_list[k] #xの方向にマスを動かす
                y += y_move_list[k] #yの方向にマスを動かす
                x %= n              #x方向でマス外に出たらx座標の先頭のほうに来るようにする
                x += n              #
                y %= n              #y方向でマス外に出たらy座標の先頭のほうに来るようにする
                y += n
                x %= n             
                y %= n
                print(x)
                print(y)
            
            ans = max(ans,now) #より大きい値に更新していく


print(ans)



