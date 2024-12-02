from array import *

a = array('i',[])
x = int(input("Enter the size:"))
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)

print(a)