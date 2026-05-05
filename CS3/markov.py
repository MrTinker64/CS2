def get_k_gram(text, position, k):
    text+=text
    return text[position:position+k]

print(get_k_gram('parisa', 5, 4))