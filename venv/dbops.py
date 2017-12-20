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

print e1.name,e1.age

db = pymysql.connect("localhost","root","","auribises" )

cursor = db.cursor()

sqlQuery = """INSERT INTO Employee(EID,
         ENAME, EAGE )
         VALUES (null, 'Jack', 27)"""

#Transaction
try:
   cursor.execute(sqlQuery)
   db.commit()
except:
   db.rollback()

db.close()

print "Db Operation Done"