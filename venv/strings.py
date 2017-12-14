name = "John Watson"
print name

l = len(name)

print l

print name[0]
print name[l-1]

print name[-11]

# 0 to l-1 , -1 to -l

str1 = "Hello"
str2 = "World"

str3 = str1 + str2

a = 10

#str4 = str1 + a

print str3

print 5 * str1
print str2 * 5

str4 = "   John, Jennie, Jack, Jim and Joe are Together.mp3"

print "John" in str4
print "George" not in str4

str5 = "Hello"
str6 = "hello"

print str1 == str5

print str6 > str5

print str4[0:5]
print str4[7:9]
print str4[7:]
print str4[:5]

str7 = str4[:2]+str4[9:]
print "str7 is: ",str7

str8 = "george"
str9 = str8.capitalize()
print str8
print str9

str10 = str8.upper()
print str10

str11 = str8.lower()
print str11

str12 = str4.rstrip()
print str12

ch = "J"

print str4.count(ch,0,len(str4))

print str4.endswith(".mp3")

print str4.find("John")

cipher = "abcdefghijklmnopqrstuvwxyz"

print cipher[0]

