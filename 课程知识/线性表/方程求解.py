def fx(x):
    return x**3-x**2*5+10*x-80
def dao(x):
    return x**2*3-10*x+10
ans=6
while '{:.9f}'.format(fx(ans))!='0.'+'0'*9:
    ans=ans-fx(ans)/dao(ans)

print('{:.9f}'.format(ans))