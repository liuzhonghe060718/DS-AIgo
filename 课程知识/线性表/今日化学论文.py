stack=[]
s=list(input())
n=len(s)
x=0
while x<n:
    if s[x]=='[':
        x+=1
        continue
    elif s[x]==']':
        word=stack.pop()
        if stack and isinstance(stack[-1],int):
            num=stack.pop()
            if stack and isinstance(stack[-1],str):
                next_word=stack.pop()
                stack.append(next_word+num*word)
            else:
                stack.append(num*word)
        else:
            stack.append(word)
    elif s[x] in '0123456789':
        start=x
        while x<n-1 and s[x+1] in '0123456789':
            x+=1
        stack.append(int(''.join(s[start:x+1])))
    else:
        stack.append(s[x])
    while len(stack)>=2 and isinstance(stack[-1],str) and isinstance(stack[-2],str):
        a,b=stack.pop(),stack.pop()
        stack.append(b+a)
    x+=1
print(stack[0])