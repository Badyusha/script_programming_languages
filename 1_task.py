# Вывести на экран все простые числа в заданном диапазоне 
# (диапазон вводится с клавиатуры)

left_range = int(input("Enter left range: "))
right_range = int(input("Enter right range: "))

for elem in range(left_range, right_range + 1):
    flag = 0
    for el in range(left_range, right_range + 1):
        if elem == 1:
            break
        if flag > 2:
            break
        if el != 0 and elem % el == 0:
            flag = flag + 1
    if flag == 2:
        print(elem)
