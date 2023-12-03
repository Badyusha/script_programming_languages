# Преобразовать текст в кортеж слов с удалением знаков  препинания.

text = input("Enter text: ")

my_list = []

index = 0

while index < len(text):
    temp = ""

    while  index < len(text) and text[index] not in " .,!?":
        temp += text[index]
        index = index + 1

    if temp != "":
        my_list.append(temp)

    index = index + 1

print(tuple(my_list))
