from collections import deque
n,m=map(int,input().split())
nums=list(map(int,input().split()))
queue=deque([i for i in range(n)])
while queue:
    a=queue.popleft()
    nums[a]-=m
    if nums[a]>0:
        queue.append(a)
print(a+1)

