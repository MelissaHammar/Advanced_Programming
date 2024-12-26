#List Initialization and Append

numbers=[]
shoe_size=[]
#in this case i am not letting the user enter the values
#filling the list using the append method in a for loop
for a in range(5):
 numbers.append(a+1)
 shoe_size.append(a+8)
#printing the lists
print(numbers)
print(shoe_size)

#Bonus
# 1-handling duplicates
while True:
    value_numbers=int(input("please enter a value to add to numbers(-1 to quit): "))
    if value_numbers==-1: break
    elif value_numbers in numbers:
         print("Cannot add this value, it already exists")
    else:
         numbers.append(value_numbers)
#printing the new version of 
print(numbers)

# 2- Already Done
# 3- Combining the two lists 
combine=numbers+shoe_size
print("the list combining both the lists: ",combine)


