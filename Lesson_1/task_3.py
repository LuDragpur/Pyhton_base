number = input("Введи любое число от 0: ")
# number_2 = int(number + number)
# number_3 = int(number + number + number)
number_2 = int(f"{number}{number}")
number_3 = int(f"{number}{number}{number}")
print(f"{number} + {number_2} + {number_3} = {int(number) + number_2 + number_3}")

