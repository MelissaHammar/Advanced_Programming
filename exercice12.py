#Rectangle of hashes
w=int(input("Width: "))
h=int(input("Height: "))
hash=""
for j in range(h):
    for i in range(w):
        hash=hash+"#"
    hash=hash+" "       
print(f"{hash}")