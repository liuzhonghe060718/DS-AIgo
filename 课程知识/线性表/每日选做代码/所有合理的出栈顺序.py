n=int(input())
def sorting(x):
    if x==1:
        return [[1]]
    else:
        s=sorting(x-1)
        s_1=[]
        for j in s:
             for i in range(x):
                 s_1.append(j[:i]+[x]+j[i:])
        s=s_1
        return s
def check(nums):
    stack=[1]
    k=1
    ans=True
    for num in nums:
        if not stack:
            k+=1
            stack.append(k)
        if stack[-1]>num:
            ans=False
            break
        while stack[-1]<num:
            k+=1
            stack.append(k)
        stack.pop()
    return ans
numbers=sorting(n)
number=[]
for numb in numbers:
    if check(numb):
        number.append(numb)
number.sort()
for i in number:
    print(' '.join(map(str,i)))

