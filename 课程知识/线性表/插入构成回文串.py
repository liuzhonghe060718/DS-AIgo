n=int(input())
s=input()
dps=[0 for _ in range(n)]
dpb=[0 for _ in range(n)]

dp=[[0 for _ in range(n)]for _ in range(n)]
for length in range(2,n+1):
    for i in range(n-length+1):
        j=i+length-1
        if s[j]==s[i]:
            dp[i][j]=dp[i+1][j-1] if length>2 else 0
        else:
            dp[i][j]=min(dp[i+1][j],dp[i][j-1])+1
print(dp[0][n-1])