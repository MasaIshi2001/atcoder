from functools import lru_cache
 
n = int(input())
 
@lru_cache(maxsize=1000)
def fc(num):
    if num <= 0:
        return 1
    else:
        return fc(num//2) + fc(num//3)
 
print(fc(n))



