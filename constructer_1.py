class A:
    def __init__(self):
        print("in A init")

    def feature_1(self):
        print("from feature_1 of A")

    def feature_2(self):
        print("from feature_2 of A")


class B:
    def __init__(self):
        print("in B init")

    def feature_1(self):
        print("from feature_1 of B")

    def feature_2(self):
        print("from feature_2 of B")




class C(B):  # cls c inherits the cls B...


    def feature_3(self):
        print("from feature_3 of C")

    def feature_5(self):
        print("from feature_5 of C")

class D(A, B):
    def __init__(self):
        super().__init__()  # to call cons.. of super cls we need to use super key..
        print("in D init")

    def feat(self):
        super().feature_2() # with help of super key we can call methods of super clss..





b1 = C()          # if we try to print constructor of child cls thn ,
           # at first its check for own constructor thn go to the super cls..
           # if it have own cons.. thn it prints that ..


d1 = D()         # here we want to pt the cons. of D which inherits B,A so for printing cons..
          # obj. got confused which one should print cls A, B
          # here we use MRO(method resolution order) left most got ist priority


# same process works on methods...
d1.feature_1()  # as we know we have two methods feature_1 (from A, from B)
                # here which one called same MRO method leftest cls work ist..
d1.feat()   # with feat we can call feature_2 method with the help of super key..