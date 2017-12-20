# Write in a File
# fos = open("newFile.txt", 'w')
# data = "Search the Candle rather than cursing the darkness.."
# fos.write(data)
# print "File Contents Written"
# fos.close()

fis = open("newFile.txt", 'r')
#str = fis.read()

pos = fis.tell()
print pos

str = fis.read(10)
print str

pos = fis.tell()
print pos

str = fis.read(10)
print str

pos = fis.tell()
print pos

str = fis.read(10)
print str

pos = fis.tell()
print pos

fis.seek(0,0)
pos = fis.tell()

print pos


fis.close()

import os

# os.remove("newFile.txt")
# os.rename("newFile.txt","yourFile.txt")
# os.mkdir("PackTwo")
