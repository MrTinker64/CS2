my_model = {}

def get_k_gram(text, position, k):
    text+=text+text[0]
    return text[position:position+k]

def add_char_to_model(model, text, position, k):
    k_gram = get_k_gram(text, position, k)
    if k_gram not in model:
        model[k_gram] = {text[position+k]: 1}
    else:
        model[k_gram][text[position+k]] += 1

for i in range(3):
	 	add_char_to_model(my_model, 'fald fall', i, 3)
print(my_model)