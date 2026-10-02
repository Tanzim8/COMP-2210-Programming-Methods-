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

def encode(letter, shift):
    normalize = ord(letter) - ord("a") # zero basis
    snormalize = normalize + shift # apply shift
    msnormalize = snormalize % 26 # wrap A..Z
    final = msnormalize + ord("a") # back to code
    return chr(final) # a str again!
print(encode("b", 3))

def encode(letter, shift):
    normalize = ord(letter) - ord("a")
    snormalize = normalize + shift
    msnormalize = snormalize % 26
    final = msnormalize + ord("a")
    return chr(final)

def encode(letter, shift):
    shifted = (ord(letter) - ord("a") + shift) % 26
    return chr(shifted + ord("a"))
