t=int(input())
s=list(map(int,input().split()))
s.sort()
n=len(s)
left=0
right=n-1
ans=[s[0],s[-1]]
while left<right:
    if abs(ans[0]+ans[1]-t)>abs(s[left]+s[right]-t):
        ans=[s[left],s[right]]
    elif abs(ans[0]+ans[1]-t)==abs(s[left]+s[right]-t) and ans[0]+ans[1]>s[left]+s[right]:
        ans = [s[left], s[right]]
    if s[left]+s[right]<t:
        left+=1
    else:
        right-=1

print(ans[0]+ans[1])
