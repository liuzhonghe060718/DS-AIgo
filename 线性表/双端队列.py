class dequeue:
    def __init__(self):
        self.items=[]
    def popright(self):
        if self.items:
            self.items.pop()
    def popleft(self):
        if self.items:
            self.items.pop(0)
    def addright(self,data):
        self.items.append(data)
    def __str__(self):
        if self.items:
            return ' '.join(map(str,self.items))
        else:
            return 'NULL'
t=int(input())
for _ in range(t):
    n=int(input())
    s=dequeue()
    for _ in range(n):
        typ,num=map(int,input().split())
        if typ==1:
            s.addright(num)
        else:
            if num==0:
                s.popleft()
            else:
                s.popright()
    print(s)