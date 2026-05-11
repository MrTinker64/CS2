def pig_latin(word):
    word = word.lower().strip(".,!?;:'\"")
    if word[0] in "aeiou":
        return word + "ay"
    else:
        return pig_latin(word[1:] + word[0])
    
print(pig_latin('strengths'))