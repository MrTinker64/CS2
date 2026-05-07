import random

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
            
# Does the first 3 k_grams and their following letters
# for i in range(3):
# 	 	add_char_to_model(my_model, 'fald fall', i, 3)
        
def build_model(text, k):
    the_model = {}
    for i in range(len(text)):
        add_char_to_model(the_model, text, i, k)
    return the_model

def next_character_frequency(model, k_gram, character):
    if k_gram not in model:
        return 0
    elif character not in model[k_gram]:
        return 0
    else:
        return model[k_gram][character]
    
def random_character(model, k_gram):
    chars = list(model[k_gram].keys())
    freqs = list(model[k_gram].values())
    total = sum(freqs)
    weights = [f / total for f in freqs]
    return random.choices(chars, weights=weights, k=1)[0]

def generate_random_text(model, length):
    seed = random.choice(list(model.keys()))
    text = seed
    for i in range(length - len(seed)):
        next_char = random_character(model, seed)
        text += next_char
        seed = seed[1:] + next_char
    return text

f = open("complete_shakespeare.txt","r")
text = f.read()
my_model = build_model(text, 7)
print(generate_random_text(my_model, 100))