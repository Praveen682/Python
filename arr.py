from array import *

arr = array('i',[1,2,3,6,3,2,4,13,3,5,6,6,3,3,1,5,4,3])
val = int(input("Enter the value to be searched:"))

c = []

for i in range(len(arr)):
    if val == arr[i]:
        c.append(i)

print(c)
