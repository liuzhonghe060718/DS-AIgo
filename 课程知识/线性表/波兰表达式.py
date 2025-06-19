s=list(input().split())
stack=[]
n=len(s)
for i in range(n):
    if s[i] in {'+','-','*','/'}:
        stack.append(s[i])
    else:
        stack.append(float(s[i]))
    while len(stack)>=3 and isinstance(stack[-1],float) and isinstance(stack[-2],float):
        b,a=stack.pop(),stack.pop()
        symbol=stack.pop()
        if symbol=='+':
            stack.append(a+b)
        elif symbol=='-':
            stack.append(a-b)
        elif symbol=='*':
            stack.append(a*b)
        else:
            stack.append(a/b)
print('{:.6f}'.format(stack[0]))