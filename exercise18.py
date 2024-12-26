#Interactive list operations

numbers = [1, 2, 3, 4, 5]
while True:
    choice=int(input("Menu\n1. Append\n2. Insert\n3. Pop\n4. Remove\n5. Quit\nEnter your choice: "))
    value=int(input("Enter value: "))
    if choice==1:
      numbers.append(value)
      print("Updated List : ",numbers)  
    elif choice==2:
      index=int(input("Enter index"))
      numbers.insert(index,value)
      print("Updated List : ",numbers)      
    elif choice==3:
      numbers.pop(value)
      print("Updated List : ",numbers)  
    elif choice==4:
       numbers.remove(value)
       print("Updated List : ",numbers)     
    elif choice==5: break
    else: print("Unvalid Choice.")