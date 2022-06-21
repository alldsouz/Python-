class car():

    def __init__(self):
        self.mileage=10
        self.name="tata"

c2=car()
c1=car()

c1.name="kia"
c2.name="toyota"

c1.mileage=12
c2.mileage=9

print(c1.mileage, c1.name)
print(c2.mileage, c2.name)