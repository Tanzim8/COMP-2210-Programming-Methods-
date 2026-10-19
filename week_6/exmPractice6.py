text = "Hello 2026"

def count_characters(text):
    new_text = text.lower()
    letter_app = {}
    for char in new_text:
        if not new_text.isdigit():
            letter_app[char] = letter_app.get(char,0)+1
    return letter_app 
print(count_characters(text))
        