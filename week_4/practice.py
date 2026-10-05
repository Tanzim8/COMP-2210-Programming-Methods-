str = " Ganzafar Latif"
digits = "123456"
str2 = "Latif"
myList = [1,2,3,4,5,6]
if str.startswith("G") and str.endswith("f"):
    print("Name starts with G ends with f.")
else:
    print("Name doesnt starts with F and ends with f. ")

print(str.isalpha())
print(digits.isdigit())
print(str.find("z"))
print(str.lower())
print(str.upper())
#removes spaces in th ebegining and the end
print(str.strip())
print(str.replace("a", "A"))
print(str.split("a"))
print(str.join(digits))
print(str.join(str2))

marks = 97.563
print(str,digits)
print(f"[str] recieved scores of {marks}")
print(f"[str] recieved scores of {marks:.1f}")
print(f"{str:>19}| {marks:6.2f}")