class student:
    school = 'DPS'
    add = 'DEOGHAR'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def show(self):
        print("the marks are : ", self.m1, self.m2, self.m3)
    @classmethod  # decorators for class method
    def info(cls):
        return cls.add

    @staticmethod # decorators for static method
    def stat():
        print("this is a static method which is not related to cls or obj. ")













s1 = student(95, 76, 94)
s2 = student(86, 70, 44)
print(s1.avg(), s2.avg())
s1.show()
s2.show()
print("the school of student is ", s1.school)
print("the address of the students is :", student.info())
print(student.stat())