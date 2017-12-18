print "Program Started..."

a = 10
b = 0
c = 0

try:
    c = a/b
except ZeroDivisionError:
    print "This is an error at run time. div by 0"
finally:
    print "This is finally"

print "c is: ",c

print "Program Finished..."