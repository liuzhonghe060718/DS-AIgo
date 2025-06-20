while True:
    n=int(input())
    if n==0:
        break
    nums=[]
    idx = {}
    for i in range(n):
        a=int(input())
        nums.append(a)
        idx[a]=i
    numbers=sorted(nums)
    ans=0

    for j in range(n):
        idx0=idx[numbers[j]]
        if idx0>j:
            ans+=(idx0-j)
            for key in idx:
                if idx[key]<idx0:
                    idx[key]+=1

        elif idx0<j:
            ans+=(j-idx0)
            for key in idx:
                if idx[key]>idx0:
                    idx[key]-=1
        del idx[numbers[j]]
    print(ans)

