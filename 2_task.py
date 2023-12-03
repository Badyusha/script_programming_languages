# С клавиатуры вводится текст, определить, сколько в нём гласных,
# а сколько согласных. В случае равенства вывести на экран все
# гласные  буквы. Посчитать количество слов в тексте.

import re

text = input("Enter text: ")

consonants = 0
vowels = 0

all_vowels = []

for letter in text:
    if letter.lower() in "eyuioaеаоэяию":
        vowels += 1
        all_vowels.append(letter.lower())

    else:
        consonants += 1 

if(consonants == vowels):
    print(all_vowels)
else:
    print(vowels, " vowels and ", consonants, " consonants\n")

print("In the text ", len(text.split()), " words")

