sentence = "python is easy and python is powerful"

def count_words(sentence):
    words_dict = {}
    for words in sentence.split():
        words_dict[words] = words_dict.get(words, 0) +1
    return words_dict
print(count_words(sentence))