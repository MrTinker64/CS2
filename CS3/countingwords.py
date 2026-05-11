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

def top_n_words(text,n):
    counts = count_words(text)
    sorted_words = sorted(counts, key=lambda w: counts[w], reverse=True)
    return sorted_words[:n]

print(top_n_words("Hello my name is Hello Hello.", 2))