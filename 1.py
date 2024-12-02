from array import *

a = array('i',[])
x = int(input("Enter the days:"))
for i in range(x):
    y = int(input())
    a.append(y)

b = []

for i in range(0,len(a),2):
    b.append(a[i])

tot = 0

for i in b:
    tot = tot+i

print(tot)


