import array as arr

a = arr.array('i',[2,3,4,7,5,7,3,5,3,7,3,2,1,7])

c = []

val = int(input("Enter the number:"))

for i in range(len(a)):
    if a[i] == val:
        c.append(i)

print("the indexes of",val,"is:",c)    
print("the total count is:",a.count(val))

