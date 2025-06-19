from bisect import bisect_left
from collections import deque
class Queue:
    def __init__(self):
        self.lis=[]
        self.size=0
        self.content=deque([])
    def add(self,x):
        x=int(x)
        self.content.append(x)
        self.size+=1
        idx=bisect_left(self.lis,x)
        self.lis.insert(idx,x)
    def __del__(self):
        num=self.content.popleft()
        idx=bisect_left(self.lis,num)
        self.lis.pop(idx)
        self.size-=1
    def query(self):
        if self.size%2==1:
            return self.lis[self.size//2]
        else:
            return '{:g}'.format((self.lis[self.size//2]+self.lis[self.size//2-1])/2)
n=int(input())
s=Queue()
for _ in range(n):
    order=input()
    if order=='del':
        s.__del__()
    elif order=='query':
        print(s.query())
    else:
        s.add(order[4:])