n,c=map(int,input().split())
places=[]
for _ in range(n):
    places.append(int(input()))
places.sort()
left,right=1,places[-1]
def check(x):
    number=1
    now_dic=0
    for i in range(1,n):
        if now_dic+places[i]-places[i-1]>=x:
            number+=1
            now_dic=0
        else:
            now_dic+=places[i]-places[i-1]
    if number>=c:
        return True
    return False
while left<=right:
    mid=(left+right)//2
    if check(mid):
        left=mid+1
    else:
        right=mid-1
print(right)
