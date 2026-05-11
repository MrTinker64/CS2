def pig_latin(word):
    word = word.lower().strip(".,!?;:'\"")
    if word[0] in "aeiouy":
        return word + "ay"
    elif "--" in word:
        return word
    else:
        return pig_latin(word[1:] + word[0])

def izzle(word):
    vowels = "aeiouy"
    last_vowel = -1
    word = word.lower().strip(".,!?;:'\"")
    for i in range(len(word)):
        if word[i] in vowels:
            last_vowel = i
    if last_vowel <= 0:
        return word + "izzle"
    return word[:last_vowel] + "izzle"

def apply_language_game(text, game):
    new_text = ""
    for word in text.split():
        new_text += game(word) + " "
    return new_text

text = open("gettysburg.txt", "r").read()
print(apply_language_game(text,izzle))