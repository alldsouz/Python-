class A:
    def featureone(self):
        print("feature 1 works")
    def featuretwo(self):
        print("feature 2 works")
# here class b inherits class A as shown below()
class B:
    def feature3(self):
        print("feature 3 works")
    def feature4(self):
        print("feature 4 works")

# class c inherits b who inherits a, this is multilevel inheritance
class C(B):
    def feature5(self):
        print("feature 5 is working")

class D (A,B):
    def feature6(self):
        print("feature 6 works")

a1=A()
a1.featureone()
a1.featuretwo()

b1=B()

c=C()
