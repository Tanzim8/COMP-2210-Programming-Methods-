myFiles = ["p1.txt", "img1.png", "p2.txt", "f1.docx", "img2.jpg"]
for myFile in myFiles:
    if ".txt" in myFile:
        print(myFile)

print(ord("a"))
print(ord("A"))

myLetters = ["l", "a", "t", "i", "f", "$"]
for letter in myLetters: 
    if ord(letter) >= 97 and ord(letter) <= 122: 
        print(chr(ord(letter)-32))
    else:
        print(letter)
