n = int(input())
h_list = list(map(int,input().split()))

for i in range(len(h_list)):
    if i == 0:
        pastH = h_list[i]
    else:
        if pastH < h_list[i]:
            pastH = h_list[i]
        else:
            print(pastH)
            exit()

