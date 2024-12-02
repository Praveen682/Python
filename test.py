from array import *

a = array('i',[2,3,4,5,6,7,2,4,6,8,10,7,5,3,2])
val = int(input("Enter the value:"))
c = []
for i in range(len(a)):
    if a[i] == val:
        c.append(i)

print("The index of the",val,"is",c)
print("The total count of",val,"is",a.count(val))