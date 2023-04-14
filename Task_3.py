number = int(input("Введите число: "))
sqr = 0
for i in range(number):
    if 2**sqr < number:
        print(f"{2**sqr}")
    sqr += 1