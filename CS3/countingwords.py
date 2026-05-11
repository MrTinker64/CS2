def remove_punctuation(text):
    result = ""
    for char in text:
        if char.isalnum() or char == " ":
            result += char
    return result

def count_words(text):
    text = remove_punctuation(text)
    words = {}
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

print(count_words("Hello my name is Hello Hello."))