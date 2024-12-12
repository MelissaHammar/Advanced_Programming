#Leap year
year=int(input("please type in a year: "))
if year%4==0:
    print("that year is a leap year")
elif year%100==0 and year%400==0:
    print("that year is a leap year")
else: print("that year is not a leap year")
#error in the given sample output: 
#1800 should be a leap because 1800/4=450
