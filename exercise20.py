#sorted list builder

user_list=[]

while True:
    value=int(input("enter a value to add: "))
    if value!=0: #verify that the entered value is not zero
        user_list.append(value)
        print("Current List",user_list)
        user_list.sort(reverse=True)
        #using sort() to sort the list and reverse=True to make the order ascending
        print("Sorted List",user_list)
    else: break
        