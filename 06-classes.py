# --------------------
# class definition
class myClass():

    def method1(self):
        print("myClass.method1()")

    def method2(self, someString):
        print("myClass.method2() " + someString)


# --------------------
# inheritance
class subClass(myClass):

    def method1(self):
        myClass.method1(self) # call method on superclass
        print("subClass.method1()")

    def method2(self, someString):
        print("subClass.method2()")


def main():
    print("Testing myClass:")
    c = myClass()
    c.method1()
    c.method2("argument myclass")

    print("Testing subClass:")
    sub=subClass()
    sub.method1()
    sub.method2("argument subclass")


# --------------------
if __name__ == "__main__":
    main()
