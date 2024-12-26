#Mutability in Lists

numbers = [1, 2, 3, 4, 5]
while 1==1: 
 index=int(input("please type in an index (-1 to Exit): "))
 #verify the index
 if index==-1: break
 else:
     value=int(input("plase type in a new value: "))
     numbers.insert(index,value)
#infinite loop with break inside if a condition is satisfied (index==-1)
print(numbers)