import pymysql

db = pymysql.connect("localhost","root","","auribises" )

cursor = db.cursor()

sql = "SELECT * FROM Employee"

try:
   cursor.execute(sql)

   results = cursor.fetchall()
   print results
   #
   # results = cursor.fetchone()
   # print results
   #
   # results = cursor.fetchone()
   # print results


   # for row in results:
   #    print row[0],row[1],row[2]

except:
   print "Error: unable to fecth data"

db.close()