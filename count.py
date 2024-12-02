from array import *

a = array('i',[])

x = int(input("Enter the size:"))
for i in range(x):
    y = int(input("Enter the elements:"))
    a.append(y)

uniq = []
dup = []

for i in a:
    if i not in uniq:
        uniq.append(i)
    else:
        dup.append(i)

print(dup)