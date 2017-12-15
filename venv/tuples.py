#Immutable
tpl = (10,20,'hello',)

print "tpl is: ",tpl

tpl1 = ()

tpl2 = (10,)

print "tpl1 is: ",tpl1
print "tpl2 is: ",tpl2

tpl3 = tpl,(1,2,3)
print "tpl3 is: ",tpl3

print "tpl[0] is: ",tpl[0]
print "tpl3[0] is: ",tpl3[0]
print "tpl3[0][0] is: ",tpl3[0][0]

# Slicing
print tpl[0:2]

print tpl[-1]

t1 = ('a','b','c')
t2 = (1,2,3)

t3 = t1+t2
print "tuple is: ",t3

print t3*2

#del t3

#print t3

print  min(t3)
print  max(t3)

print len(t3)

c = cmp(t1,t3)
print c