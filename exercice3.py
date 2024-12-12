#Discount Calculation 
amount=float(input("Total amount: "))
items=int(input("number of items: "))
day=input("Day of the week: ")
price=0

if day=="saturday" or day=="sunday":
    price=amount-(amount*0.2)
elif day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
    price=amount-(amount*0.1)
else: print("That is not a day of the week!")

if items>5:
    price=amount-amount*0.25
    
print(f"Total price after dictount {price} Dinars")