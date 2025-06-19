from functools import lru_cache
n=int(input())
value=[0]+list(map(int,input().split()))
@lru_cache(None)
def dfs(i):
    if i>n:
        return (0,0)
    left=i*2
    right=i*2+1
    l0,l1=dfs(left)
    r0,r1=dfs(right)
    not_take=max(l0,l1)+max(r0,r1)
    take=value[i]+l0+r0
    return (not_take,take)
print(max(dfs(1)))