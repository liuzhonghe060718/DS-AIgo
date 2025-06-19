import math
class Fraction:
    def __init__(self,son,monther):
        self.son=son
        self.mother=monther
    def __add__(self, other):
        new_son=self.son*other.mother+self.mother*other.son
        new_mother=self.mother*other.mother
        m=math.gcd(new_son,new_mother)
        return Fraction(new_son//m,new_mother//m)
    def __str__(self):
        return str(self.son)+'/'+str(self.mother)
a,b,c,d=map(int,input().split())
print(Fraction(a,b)+Fraction(c,d))