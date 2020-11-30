revenue = float(input("Введите значение Вашей выручки (рубли): "))
costs = float(input("Введите значение Ваших издержек (рубли): "))
result = revenue - costs
if result > 0:
    print(f"Отлично! Ваша компания работает с прибылью {result} рублей!")
    print(f"Рентабильность выручки составила {result / revenue:.3f}")
    personal = int(input("Сколько сотрудников работает в Вашей компании? "))
    print(f"Если разделить прибыль между сотрудниками, то каждый получит по {result / personal:.3f} рублей. ")
elif result < 0:
    print(f"Ваша компания сработала с убытком {result} рублей")

