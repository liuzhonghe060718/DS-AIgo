from collections import deque
def bfs(k):
    queue=deque([1])
    while queue:
        num=queue.popleft()
        if num%k==0:
            return num
        queue.append(num*10)
        queue.append(num*10+1)

while True:
    n=int(input())
    if n==0:
        break
    print(bfs(n))

