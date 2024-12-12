#Name length kingdom
t=[]
b=True
while b==True :
   x=input("city: ")
   if x.lower()!="stop":
    t.append(x)
   else: b=False
   
   
for x in t:
    print(f"the city {x} has {len(x)} letters,  so its population is {len(x)*1000000}")  