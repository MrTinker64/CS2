def count_words(text):
    words = {}
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

print(count_words("Hello my name is Hello Hello"))