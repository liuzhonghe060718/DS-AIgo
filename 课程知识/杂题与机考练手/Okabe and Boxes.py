n=int(input())
stack=[]
ans=0
idx=1
for i in range(2*n):
    s=input()
    if s[0]=='a':
        stack.append(int(s[4:]))
    else:
        if stack[-1]!=idx:
            stack.sort(reverse=True)
            ans+=1
        stack.pop()
        idx+=1
print(ans)
