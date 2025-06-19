n=int(input())
cards=list(input().split())
number=[[] for _ in range(9)]
for c in cards:
    number[int(c[1])-1].append(c)
for i in range(9):
    print(f'Queue{i+1}:'+' '.join(number[i]))
s={'A':[],'B':[],'C':[],'D':[]}
for i in range(9):
    for c in number[i]:
        s[c[0]].append(c)
ans=[]
for k,v in s.items():
    print(f'Queue{k}:'+' '.join(v))
    ans.extend(v)
print(' '.join(ans))

