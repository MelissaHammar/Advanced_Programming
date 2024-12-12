#Framed word
word=input("please enter a word")
line=""
for i in range(30): line=line+"*"
print(line)
x=""
for i in range((28-len(word))//2):
    x=x+" "
if(len(word)%2!=0):
    x="*"+x+" "+word+x+"*"
else: x="*"+x+word+x+"*"
print(x)

print(line)