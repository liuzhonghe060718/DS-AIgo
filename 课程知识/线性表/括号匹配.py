
while True:
    try:
        s=list(input())
    except EOFError:
        break
    stack=[]
    n=len(s)
    ans=[' ']*n
    for i in range(n):
        if s[i]=='(':
            stack.append(i)
        elif s[i]==')':
            if stack:
                stack.pop()
            else:
                ans[i]='?'
    for k in stack:
        ans[k]='$'
    print(''.join(s))
    print(''.join(ans))