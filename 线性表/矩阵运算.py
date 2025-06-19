matrix=[[]for _ in range(3)]
nums=[]

for i in range(3):
    row,col=map(int,input().split())
    nums.append([row,col])
    for j in range(row):
        matrix[i].append(list(map(int,input().split())))
ans=[[0 for _ in range(nums[1][1])]for _ in range(nums[0][0])]
if nums[0][1]!=nums[1][0] or nums[0][0]!=nums[2][0] or nums[1][1]!=nums[2][1]:
    print('Error!')
    exit()
for i in range(nums[0][0]):
    for j in range(nums[1][1]):
        for x in range(nums[0][1]):
            ans[i][j]+=matrix[0][i][x]*matrix[1][x][j]
        ans[i][j]+=matrix[2][i][j]
for i in range(nums[0][0]):
    print(' '.join(map(str,ans[i])))