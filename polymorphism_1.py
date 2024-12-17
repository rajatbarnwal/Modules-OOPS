# IN PYTHON THERE ARE FOUR WAYS TO IMPLEMENTATION OF POLYMORPHISM...
#  1 DUCK TYPING
#  2 OPERATOR OVERLOADING
#  3 METHOD OVERLOADING
#  4 METHOD OVERRIDING

# DUCK TYPING

class PYCHARM:
    def execute(self):
        print("compiling!")
        print("running!!")

class My_charm:
    def execute(self):
        print("build@@")
        print("count no of lines@")
        print("compiling!")
        print("running!!")


class LAPPY:
    def code(self, ide):
        ide.execute()



# ide = PYCHARM()
               # if we have obj. ide having method execute() then it'll work..
               # its not concern about in which class ide(obj.) belongs..
               # if a bird can walk like a duck, can swim like a duck thn it should be a duck...(duck typing)
ide = My_charm()
lap1 = LAPPY()
lap1.code(ide)