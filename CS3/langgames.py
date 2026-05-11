def pig_latin(word):
    word = word.lower().strip(".,!?;:'\"")
    if word[0] in "aeiou":
        return word + "ay"
    else:
        return pig_latin(word[1:] + word[0])

def izzle(word):
    vowels = "aeiouy"
    last_vowel = -1
    for i in range(len(word)):
        if word[i].lower() in vowels:
            last_vowel = i
    if last_vowel <= 0:
        return word + "izzle"
    return word[:last_vowel] + "izzle"

print(izzle("Merry Christmas"))