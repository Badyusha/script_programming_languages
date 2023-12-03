# Реализуйте программу «Кондитерская», которая будет включать  в себя шесть пунктов меню. У вас есть словарь,
# где ключ – название  продукции (торт, пирожное, маффин и т.д.). Значение – список,  который содержит
# состав, цену (за 100гр) и кол-во (в граммах).  
# 1. Просмотр описания: название – описание 
# 2. Просмотр цены: название – цена. 
# 3. Просмотр количества: название – количество. 
# 4. Всю информацию. 
# 5. Покупка 
# В пункте «Покупка» необходимо совершить покупку, с клавиатуры вводите название продукции
# и его кол-во, n – выход из  программы. Посчитать цену выбранных товаров и сколько товаров  осталось в изначальном списке 
# 6. До свидания

confectionery_menu = {
    "Торт": ["Вкусный торт с разными начинками.", 200, 500],
    "Пирожное": ["Нежное пирожное с шоколадом.", 150, 300],
    "Маффин": ["Ароматный маффин с ягодами.", 100, 400],
    "Печенье": ["Хрустящее печенье с орехами.", 120, 350],
    "Эклер": ["Воздушный эклер с заварным кремом.", 180, 250],
    "Шоколадка": ["Темный шоколад с миндалем.", 250, 200]
}

def display_description():
    for product, description in confectionery_menu.items():
        print(f"{product} – {description[0]}")

def display_price():
    for product, details in confectionery_menu.items():
        print(f"{product} – Цена: {details[1]} руб. за 100 г")

def display_quantity():
    for product, details in confectionery_menu.items():
        print(f"{product} – Количество: {details[2]} г")

def display_all_info():
    for product, details in confectionery_menu.items():
        print(f"{product} – Описание: {details[0]}, Цена: {details[1]} руб. за 100 г, Количество: {details[2]} г")

def buy_product():
    total_cost = 0
    while True:
        product = input("Введите название продукции (n - выход из программы): ").strip()
        if product == "n":
            break
        if product in confectionery_menu:
            quantity = int(input(f"Введите количество {product} (в граммах): ").strip())
            if quantity <= confectionery_menu[product][2]:
                cost = (quantity / 100) * confectionery_menu[product][1]
                confectionery_menu[product][2] -= quantity
                total_cost += cost
                print(f"Вы купили {quantity} г {product} за {cost} руб.")
            else:
                print(f"Извините, недостаточно {product} на складе.")
        else:
            print("Продукция не найдена в меню. Попробуйте снова.")

    print(f"Итого к оплате: {total_cost} руб.")
    print("Остатки на складе:")
    display_quantity()

while True:
    print("\nМеню Кондитерской:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите опцию (1/2/3/4/5/6): ").strip()

    if choice == "1":
        display_description()
    elif choice == "2":
        display_price()
    elif choice == "3":
        display_quantity()
    elif choice == "4":
        display_all_info()
    elif choice == "5":
        buy_product()
    elif choice == "6":
        print("Спасибо за посещение! До свидания.")
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")

