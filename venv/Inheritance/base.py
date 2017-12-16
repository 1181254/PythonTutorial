class Parent:

    def sayHello(self):
        print "Hello from Parent"

class Child(Parent):

    def sayHello(self):
        print "Hello from Child"

    def show(self):
        print "This is show of Child"

class GrandChild(Child):

    def sayHello(self):
        print "Hello from Grand Child"

    def show(self):
        print "This is show of GrandChild"


class A:
    def aShow(self,a):
        print "Show of A",a

class B:
    def bShow(self):
        print "Show of B"

class C(A,B):
    def cShow(self):
        #super
        print "Show of C"


c = C()
c.aShow(10)
c.bShow()
c.cShow()

ch = Child()
ch.sayHello()
ch.show()