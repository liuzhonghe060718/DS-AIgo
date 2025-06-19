import math
n=int(input())



for _ in range(n):
    number=int(input())

    def divide(num, ans):
        if num==1:
            return 1
        count=0
        for i in range(ans,num+1):
            if num % i == 0:
                count+=divide(num//i,i)
        return count
    print(divide(number,2))

