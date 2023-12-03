# Создайте словарь из строки ' Never look back' следующим  образом:
# в качестве ключей возьмите символы строки, а значениями  пусть будут
# числа, соответствующие количеству вхождений данного символа в строку.

text = ' Never look back'

dictionary = {letter: text.count(letter) for letter in text}

print(dictionary)
