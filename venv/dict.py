d1={}

d1[0] = 'John'
d1[1] = 'Jennie'
d1[102] = 'Jack'
d1['key'] = "Jennie"

d2 = {'key1':'George',0:100}

print d1
print d1[0]
print d1['key']

d1[0] = 1000
print d1

del d1[0]

print d1
print d2

print len(d1)
print len(d2)

c = cmp(d2,d1)

print "c is: ",c

print d1.keys()
print d1.values()
print d1.items()

d1.update(d2)

d3 = d1,d2

print "d1 is: ",d1
print "d2 is: ",d2
print "d3 is: ",d3