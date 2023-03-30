from collections import deque
import numpy as np

v_lis = []
for i in range(4):
    v1,v2 = (int(x) for x in input().split())
    v_lis.append([v1,v2])

hen_lis = [[v_lis[1],v_lis[2],v_lis[3]],[v_lis[0],v_lis[2],v_lis[3]],[v_lis[0],v_lis[1],v_lis[3]],[v_lis[0],v_lis[1],v_lis[2]]]
noko_lis = [v_lis[0],v_lis[1],v_lis[2],v_lis[3]]
check_lis = [0,0,0,0]
migi_cnt = 0

for i in range(len(hen_lis)):
    hen_deq = deque(hen_lis[i])
    migi_cnt = 0
    for j in range(3):
        hen_deq.rotate(1)
        ch_hen1 = np.array(hen_deq[0]) - np.array(hen_deq[1])
        ch_hen2 = np.array(noko_lis[i]) - np.array(hen_deq[1])
        gaiseki = np.cross(ch_hen1,ch_hen2)


        if gaiseki < 0:
            migi_cnt = migi_cnt + 1
            print(migi_cnt)
        
        if migi_cnt == 3:
            check_lis[i] = 1
        
    
        
   

if 1 in check_lis:
    print("No")
else:
    print("Yes")