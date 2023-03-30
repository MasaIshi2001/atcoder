from functools import lru_cache

@lru_cache(maxsize=1000)
def search(s,time):
    global hantei
    if s not in visited.keys():
        hantei = True
        return True
  
    if visited[s] == time:
        print("no")
        hantei = False
        return False

    if s in dic.keys():
        visited[s] = time
        search(dic[s],time)
    else:
        hantei = True
        return True


n = int(input())
st_lis = []
for i in range(n):
    s,t = (str(x) for x in input().split())
    st_lis.append([s,t])

dic = {}
visited = {}
for i in st_lis:
    dic[i[0]] = i[1]
    visited[i[0]] = 0

time = 1
hantei = False
for i in st_lis:
    search(i[1],time)
    if hantei == False:
        print("No")
        exit()
    else:
        print("?")
        time += 1
    # while i[1] in dic.keys():
    #     if i[1] not in visited.keys():
    #         hantei = True
    #         break
    #     if visited[i[1]] == time:
    #         print("No")
    #         exit()
    #     visited[i[1]] = time
    # time += 1


print("Yes")
