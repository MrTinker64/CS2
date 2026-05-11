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

def top_n_words_except(counts, n, boring):
    for bore in boring:
        del counts[bore]
    sorted_words = sorted(counts, key=lambda w: counts[w], reverse=True)
    return sorted_words[:n]

def average_word_lengths(counts):
    total_length = 0
    total_words = 0
    for word, frequency in counts.items():
        total_length += len(word) * frequency
        total_words += frequency
    return total_length/total_words
        

print(average_word_lengths(count_words("Hello and all")))