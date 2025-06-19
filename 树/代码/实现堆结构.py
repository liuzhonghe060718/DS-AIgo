class BinHeap:
    def __init__(self):
        self.lst=[0]
        self.size=0
    def purup(self,i):
        while i//2>0:
            if self.lst[i]<self.lst[i//2]:
                self.lst[i],self.lst[i//2]=self.lst[i//2],self.lst[i]
            i=i//2
    def insert(self,k):
        self.lst.append(k)
        self.size+=1
        self.purup(self.size)
    def minChild(self,i):#寻找较小的那个子节点方便向下调整
        if i*2+1>self.size:
            return i*2
        else:
            if self.lst[i*2]<self.lst[i*2+1]:
                return i*2
            else:
                return i*2+1
        
    def perdown(self,i):
        while i*2<=self.size:
            mc=self.minChild(i)
            if self.lst[i]>self.lst[mc]:
                self.lst[i],self.lst[mc]=self.lst[mc],self.lst[i]
            i=mc
    def pop(self):
        a=self.lst[1]
        self.lst[1]=self.lst[self.size]
        self.size-=1
        self.lst.pop()
        self.perdown(1)
        return a
    def build_heap(self,alist):#向下调整
        i=len(alist)//2#从第一个非叶子节点开始
        self.size=len(alist)
        self.lst=[0]+alist
        while i>0:
            self.perdown(i)
            i-=1
n=int(input())
nums=BinHeap()

