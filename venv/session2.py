def sayHello():
    print "This is Awesome"
    return


def sayHelloAgain(name):
    print "hello dear, ", name
    return


def printTable(num):
    for i in range(1, 11):
        print num, " ", i, "'s are ", num * i
    return


def addNums(a, b):
    c = a + b
    # print "Sum is ",c
    return c


def squareOfNum(n=3):
    sq = n * n
    print "square of ", n, " is ", sq


sayHello()
sayHelloAgain("George")
sayHelloAgain(name="Jennie")
printTable(5)
result = addNums(a=10, b=20)
print "Result is ", result
squareOfNum()


class Driver:
    driverCount = 0

    def __init__(self, name="", phone="", age=""):
        # Driver.name = "John";
        # self.name = "Jennie";

        Driver.driverCount = Driver.driverCount + 1
        self.name = name
        self.phone = phone
        self.age = age

        print "Driver Object Created"

    def showDriver(self):
        print "Driver Name: ", self.name
        print "Driver Phone: ", self.phone
        print "Driver Age: ", self.age

    def showDriverCount(self):
        print "Number of Drivers ", Driver.driverCount


d2 = Driver()

d1 = Driver("John", 989898989, 30)
d1.showDriver()
d1.showDriverCount()


class User:
    count = 0

    def __init__(self):
        User.count = User.count + 1
        print "User Object Created"

    def showUserCount(self):
        self.count = self.count + 1
        print "User Count: ", User.count
        print "Self Count is: ", self.count


u1 = User()
u1.showUserCount()

u2 = User()
u2.showUserCount()




