class student:
    school = 'DPS'
    add = 'DEOGHAR'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.lappy()  # creating the obj. of inner cls in outer cls..

    def avg(self):
        return (self.m1 + self.m2 +self.m3) / 3

    def show(self):
        print("the marks are : ", self.m1, self.m2, self.m3)
    @classmethod  # decorators for class method
    def info(cls):
        return cls.add

    class lappy:

        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i5_8th gen'

        def show(self):
            print("the info of the lappy :\n", self.brand, self.cpu)

# we can create obj of inr cls inside the outer cls or
# we can create it outside the outer cls bt thn we need to call it with the name of the outer clss.
# example we can create lap1 = student.lappy() like this










s1 = student(95, 76, 94)
s2 = student(86, 70, 44)
print(s1.avg(), s2.avg())
s1.show()
s2.show()
print("the school of student is ", s1.school)
print("the address of the students is :", student.info())
print(s1.lap.brand)  # to print inner class we need to take help of obj of the outer class
s1.lap.show()  # here we can see the two show fun are present bt both of them are diff ..