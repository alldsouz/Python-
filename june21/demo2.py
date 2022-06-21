class student():
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop

    def show(self):
        print(self.name,self.roll)
        self.lap.show()
# laptop class is inner class in student class
    class laptop():
        def __init__(self):
            self.brand='hp',
            self.cpu='i5',
            self.ram=16
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1= student('abc',123)
s2=student('xyz',234)

s1.show()
# lap1=s1.lap
