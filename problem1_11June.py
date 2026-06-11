sentence=""
x="y"

while x=="y":
    sent=input("Enter sentence to save: ")
    if sent=="END":
        break
    else:
        sentence+=(" "+sent)

with open("example.txt","w") as file:
    file.write(sentence)
    
print(sentence)

