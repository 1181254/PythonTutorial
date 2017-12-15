import strings

list1 = [10,20,30,40,50]
list7 = [10,20,30,40,50]
list2 = ['A','B','C']
list3 = ["Hello","Hi","How","Are","You"]
list4 = [1,2.2,"Hi",'A',100]

list5 = []

print list1
print list2
print list3
print list4
print list5

print list4[0]
print list4[0:2]
print list4[-1]
print list4[0:]
print list4[:2]

list6 = list1+list2

#list6 + 30

print list6

print list1 * 2
print 2*list1

list1[2] = "Wow"
list1.append(100)

del list1[0]
#del list1[3:5]

print list1

print min(list4)
print max(list4)
print len(list1)

c =  cmp(list1,list1)
print "c is: ",c

print list1.index(20)

mylist = [10,1,2,3,10,10,5,7,9]
print mylist.count(10)

print mylist.pop()

print mylist

mylist.insert(2,100)

print mylist

yourList = [1,2,3]

mylist.extend(yourList)

yourList.remove(3)

mylist.reverse()
mylist.sort()

print mylist

print yourList