my_age = 20
name = input("Как тебя зовут: ")
print(f"Привет, {name}!")
age = int(input("Сколько тебе лет: "))
if age > my_age:
    print(f"Ты старше меня на {age - my_age} лет! ")
else:
    print(f"Ты младше меня на {my_age - age} лет! ")
country = input("Из какой ты страны?\n1 - Россия, 2 - Америка, 3 - Европа\n")
if country == "1":
    print(f"Здорово! Я тоже! ")
elif country == "2":
        print(f"Ого! Я была в этой стране! ")
elif country == "3":
        print(f"Здорово! Мне нравиться Европа! ")
else:
    print(f"Интересно, хотелось бы туда съездить! ")
