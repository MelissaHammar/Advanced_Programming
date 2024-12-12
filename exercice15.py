#Vowels
x=input("please type in a string: ")
a=False
o=False
e=False
for i in x:
    if i=='e':
        e=True
    if i=='a':
       a=True
    if i=='o':
        o=True
    
if a: print("a found.")
else: print("a not found.")
if e: print("e found.")
else: print("e not found.")
if o: print("o found.")
else: print("o not found.")
