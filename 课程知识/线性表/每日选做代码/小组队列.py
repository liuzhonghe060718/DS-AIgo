class Dequeue:
    def __init__(self):
        self.queue=[]
        self.groups=[]
    def enqueue(self,data,group):
        if group in self.groups:
            idx=self.groups.index(group)
            self.queue[idx].append(data)
        else:
            self.queue.append([data])
            self.groups.append(group)
    def dequeue(self):
        if self.queue:
            member=self.queue[0].pop(0)
            if not self.queue[0]:
                self.queue.pop(0)
                self.groups.pop(0)
            return member
t=int(input())
ngroups={}
k=t
for j in range(t):
    s=list(input().split())
    for num in s:
        ngroups[num]=j
queue=Dequeue()
while True:
    a=input()
    if a=='STOP':
        break
    if a=='DEQUEUE':
        print(queue.dequeue())
    else:
        dat=a[8:]
        if dat in ngroups.keys():
            grou=ngroups[dat]
            queue.enqueue(dat,grou)
        else:
            queue.enqueue(dat,k)
            k+=1


