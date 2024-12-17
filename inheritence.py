class A:


    def fun1(self):
        print("mummy , papa")

    def fun2(self):
        print("mumma loves bhai most")

class B(A):
    def fun3(self):
        print("bhai, puchu , and me")
    def fun4(self):
        print("me:BTECH, puchu:BA(english), bhai:DIPLOMA")

class C(B):
    def fun5(self):
        print("bhai --> bahula")
        print("mumma :bahula \n puchu :bahula \n me : rajbandh ")


class D:
    def fun6(self):
        print("bhai --> DIP clg")

class E(A, D):
    def fun7(self):
        print("puchu --> KNU clg")

a1 = A()  # object of parent cls/ super cls
a1.fun1()  # bt it can fetch only its own features.
a1.fun2()

           # cls b extends cls a is called single level inheritance


b1 = B()  # sub_cls or child_cls (which extends class b)
b1.fun1()  # it can fetch both features of its own cls and its super cls also.
b1.fun2()  # that's why b1 can access all methods which belongs to cls a and b also.
b1.fun3()
b1.fun4()

c1= C()   # this is the example of multi level inheritance (c extends b extends a)
c1.fun2()
c1.fun4()
c1.fun5()
      # this is called multiple inheritance
e1= E()  # where e extends both a and d (which two r diff. classes...
e1.fun2()
e1.fun7()
