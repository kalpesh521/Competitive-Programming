#Method Overidingg
class Student:
    def __init__(self,m1,m2) :
        self.m1=m1
        self.m2=m2
    def sum (self ,a=None,b=None,c=None):
        s=0
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s
s1=Student(25,60)
print(s1.sum(23,45))


#Method Overiding 
class A:
    def show(self):
        print("In A show")
class B(A):
    # def show(self):
    #     print("In B show")
    pass
a1=B()
print(a1.show())