my_model = {}

def get_k_gram(text, position, k):
    return text[position:position+k]

def add_char_to_model(model, text, position, k):
    text+=text+text[0]
    k_gram = get_k_gram(text, position, k)
    if k_gram not in model:
        model[k_gram] = {text[position+k]: 1}
    else:
        if text[position+k] in model[k_gram]:
            model[k_gram][text[position+k]] += 1
        else:
            model[k_gram][text[position+k]] = 1
        
def build_model(text, k):
    the_model = {}
    for i in range(len(text)):
        add_char_to_model(the_model, 'fald fall', i, k)
    return the_model

# Does the first 3 k_grams and their following letters
# for i in range(3):
# 	 	add_char_to_model(my_model, 'fald fall', i, 3)

my_model = build_model('fald fall', 3)
print(my_model)
print("{'fal': {'d': 1, 'l': 1}, 'ald': {' ': 1}, 'ld ': {'f': 1}, 'd f': {'a': 1}, ' fa': {'l': 1}, 'all': {'f': 1}, 'llf': {'a': 1}, 'lfa': {'l': 1} }")