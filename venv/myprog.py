a = 100
b = 20
c = 30


if(a>b):
    if(a>c):
        print 'Greatest is: ',a
    else:
        print 'Greatest is: ', c
else:
    print 'Greatest is: ', b


for i in range(1,11):
    if(i==5):
        break
    print i

print '-------------'

j = 10
while(j>0):

    j = j - 1

    if(j>5):
        continue

    print j


for i in range(1,4):
    print '----'
    print 'i is:', i
    print '----'
    for j in range(1,4):
        print 'j is:',j


print '-------------'




