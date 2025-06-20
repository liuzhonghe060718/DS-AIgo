import heapq
n=int(input())
frequency={}
for _ in range(n):
    a,b=input().split()
    frequency[a]=int(b)
class Treenode:
    def __init__(self,val,freq):
        self.left=None
        self.right=None
        self.val=val
        self.freq=freq
    def __gt__(self, other):
        if self.freq>other.freq:
            return True
        elif self.freq==other.freq:
            return min(self.val)>min(other.val)
        else:
            return False
heap=[Treenode([val],freq) for val,freq in frequency.items()]
heapq.heapify(heap)
while len(heap)>1:
    left=heapq.heappop(heap)
    right=heapq.heappop(heap)
    new_node=Treenode(left.val+right.val,left.freq+right.freq)
    new_node.left=left
    new_node.right=right
    heapq.heappush(heap,new_node)
root=heap[0]
def answer_node(s):
    t=len(s)
    j=0
    ans=[]
    now_node=root
    while j<t:
        if s[j]=='1':
            now_node=now_node.right
        else:
            now_node=now_node.left
        if now_node.left is None and now_node.right is None:
            ans.append(now_node.val[0])
            now_node=root
        j+=1
    return ''.join(ans)
word_to_node={}
def inorder(node,nums):
    if node.left is None and node.right is None:
        word_to_node[node.val[0]]=''.join(nums)
    else:
        inorder(node.left,nums+['0'])
        inorder(node.right,nums+['1'])
inorder(root,[])
while True:
    try:
        words=input()
    except EOFError:
        break
    if words[0] in ('0','1'):
        print(answer_node(words))
    else:
        answer=[]
        for x in words:
            answer.append(word_to_node[x])
        print(''.join(answer))

