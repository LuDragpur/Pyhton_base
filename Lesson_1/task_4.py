num_init = int(input("Введите целое положительное число: "))
dig = num_init % 10
num = num_init
while num > 0:
    digit = num % 10
    if digit > dig:
        dig = digit
        if dig == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_init} равна {dig}")