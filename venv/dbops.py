import pymysql

class Employee:

    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag
        print "Employee Object Created"

    def showEmployee(self):
        print self.name, " is ",self.age," years old"



e1 = Employee("Geroge",35)
e1.showEmployee()

db = pymysql.connect("localhost","root","","auribises")

cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
cursor.execute("insert into Employee values(null,'Harry',37)")
#cursor.execute("SELECT * from Employee")
#data = cursor.fetchone()

cursor.close()

#print data

db.close()

print "Db Operation Done"