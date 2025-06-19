import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
ans=[]
lst=[-1]*m
find=[i**2 for i in range(1,m//2+1)]

for i in range(n):
    mat = 1
    idx=0
    x=num_list[i]%m
    while lst[x]!=-1 and  lst[x]!=num_list[i]:
        x=(num_list[i]%m+mat*find[idx])%m
        mat*=(-1)
        if mat==1:
            idx+=1
    ans.append(x)
    lst[x]=num_list[i]
print(' '.join(map(str,ans)))
