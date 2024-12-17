# METHOD OVERLOADING....
# IT MEANS THE METHODS(NAME) WITH DIFF. PARAMETERS DEFINE IN A CLASS IS CALLED METHOD OVERLOADING..
# IN PYTHON METHOD OVERLOADING NOT PRESENT PURELY BCOZ WE CANT DEFINE THE TWO METHODS HAVING SAME NAME IN A CLS

class A:




    def sum(self, a=None, b=None, c=None ):   # we cant use method overloading in python bt ..
         s = 0
         if a!=None and b!=None and c!=None:   # by this method we can solve the parameter prblm of methods..
            s = a + b + c
         elif a!=None and b!=None:
            s = a + b
         else:
            s = a
         return s


s1 = A()
print(s1.sum(4, 5, 6))   # its work for this
print(s1.sum(4, 7))    # this also...

