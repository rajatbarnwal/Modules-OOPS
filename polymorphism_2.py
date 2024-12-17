# 2.OPERATOR OVERLOADING...

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):   # after that if we find s3 = s1 +s2 thn it'll work..
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    def __gt__(self, other):  # now '>' its work (gt() method called for greater than operator..
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):  # now we can print directly any obj of Student cls..
        return '{} {}'.format(self.m1, self.m2)  # formatting of tuples into str...




s1 = Student(78, 69)
s2 = Student(89, 67)

# s3 = s1 + s2
  # '+' operator means __add__() bt its undefined for obj.
  # it can be work for int, float, str bt here s1 , s2 are of obj..s its doesnt have any special type..
  # so at first we need to define __add__()..

s3 = s1 +s2
print(s3.m1, s3.m2)

if s1 > s2:  # again it can't work bcoz '>' symbl undefined for obj.. so first we need to define..
    print("s1 wins")
else:
    print("s2 wins")

print(s3)  # if we want to print s3 directly bt it returns the add.. not value ..
    # so we need to overload the method __str__ ().. which is called in background while we print something.
print(s1)

# so to define methods of particular operators in class to use it in obj.. is called "OPERATOR OVERLOADING"