import math
scores=list(map(float,input().split()))
n=len(scores)
scores.sort()
num=int(n*0.4)
target=scores[num]
def cal(s,b):
    m=b/1000000000*s
    return m+1.1**m
left=0
right=10000000000
while left<right:
    mid=(left+right)//2
    if cal(target,mid)>=85:
        right=mid
    else:
        left=mid+1

print(left)
