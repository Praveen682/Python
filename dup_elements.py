from array import *

a = array('i',[])

x = int(input("Enter the size of the array:"))
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)

dup = array('i',[])

for i in a:
    if i not in dup:
        dup.append(i)

print(a)
print(dup)
