from numpy import average


class student:
    def __init__(self, m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3
    
    def average(self):
        return (self.m1+self.m2+self.m3)/3

# getters
    def getm1(self):
        return self.m1

# setter 
    def setm1(self, value):
        self.m1= value

s1= student(1,2,3)
s2= student(4,5,6)
s3= student(7,8,9)

# print(s2.average())
# print(s1.setm1(9))
print(s1.getm1())