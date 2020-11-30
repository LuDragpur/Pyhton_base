sec = int(input("Введи любое число в секундах:"))
h = sec // 3600
m = sec // 60 - h * 60
s = sec % 60
print(f"{h:2}:{m:02}:{s:02}")


