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
        add_char_to_model(the_model, 'fald fall', i, k)
    return the_model

def next_character_frequency(model, k_gram, character):
    if k_gram not in model:
        return 0
    elif character not in model[k_gram]:
        return 0
    else:
        return model[k_gram][character]

my_model = {'ald': {' ': 1},'fal': {'d': 1,'l': 1}}
print(next_character_frequency(my_model, 'flu', 'f'))