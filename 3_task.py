# Дан список чисел. Удалить в списке все числа,
# которые  повторяются более двух раз.
# Отсортировать список по убыванию.

from itertools import groupby

list_len = int(input("Enter list length: "))

my_list = []

for list_elem in range(list_len):
    list_elem = int(input("Enter list element: "))
    my_list.append(list_elem)

my_list.sort(reverse=True)

new_list = [el for el, _ in groupby(my_list)]

print(new_list)