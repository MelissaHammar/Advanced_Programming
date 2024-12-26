#unique words

words=set()
while True:
    word=input("Please enter a word: ").strip()#strip() is used to ignore whitespace
    if word in words: 
        break
    else : 
        words.add(word) 
        print(words)
print("you typed : ",len(words),"unique words")
#len(words) because the sets ignore duplicates and we made sure there were none