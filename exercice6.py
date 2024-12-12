#Separating Dinars and Centimes
price=float(input("please type in a price: "))
dinars=int(price)
centimes=int((price-dinars)*100) #to get only 2 digits after the floating point
print("dinars: ",dinars)
print("centimes: ",centimes)