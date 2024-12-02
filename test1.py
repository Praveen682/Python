import array as arra

arr = arra.array('i',[2,3,4,5,6,7,7,8,9,9,8,7,7,5,6,4,7,7,7])

val = int(input("Enter the number:"))

c = []

for i in range(len(arr)):
    if arr[i] == val:
        c.append(i)

print("the index of the number are:",c)
print("the total count of the number is:",arr.count(val))
