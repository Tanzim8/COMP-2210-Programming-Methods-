sentence = "Python is fun and Python is powerful and Python is easy"

def word_frequency(sentence):
    new_sentace_lower = sentence.lower()
    sentence_split = new_sentace_lower.split(" ")
    new_dict = {}
    for word in sentence_split: 
        new_dict[word] = new_dict.get(word, 0) +1
    return new_dict
print(word_frequency(sentence))
