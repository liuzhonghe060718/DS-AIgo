n=int(input())
matrix=[[0 for _ in range(n)]for _ in range(n)]
idx=0
while idx<n*n:
    s=list(map(int,input().split()))
    for x in s:
        matrix[idx//n][idx%n]=x
        idx+=1
def find(nums):
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(1,n):
        if dp[i-1]<0:
            dp[i]=nums[i]
        else:
            dp[i]=dp[i-1]+nums[i]
    return max(dp)
ans=float('-inf')
for i in range(n):
    for j in range(i+1,n):
        new_num=[0]*n
        for x in range(i,j+1):
            for y in range(n):
                new_num[y]+=matrix[x][y]
        ans=max(ans,find(new_num))
print(ans)



