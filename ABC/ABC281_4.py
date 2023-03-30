n,k,d = (int(x) for x in input().split())
a_list = list(map(int,input().split()))

a_dict = {}
for i in a_list:
    if i%d not in a_dict:
        a_dict[i%d] = []
    a_dict[i%d].append(i)


