#Palindrome
word=input("please type in a word: ")
i=0
b=True
j=len(word)-1
if len(word)%2==0: print("No, it's not a palindrome")
else:
    while i!=j and b:
        if word[i]==word[j]:
            i=i+1
            j=j-1
        else: b=False
    if b: print("yes, it's a palindrome")
    else : print("No, it's not a palindrome")
        
        

    
        
