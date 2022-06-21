class A:
    def __init__(self):
        print("A initialized")
    def featureone(self):
        print("feature 1 works")
    def featuretwo(self):
        print("feature 2 works")

# here class b inherits class A as shown below()

class B:
    def __init__(self):
        super().__init__()
        print("B initialized")
    def feature3(self):
        print("feature 3 works")
    def feature4(self):
        print("feature 4 works")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C initialized")
a1= C()
