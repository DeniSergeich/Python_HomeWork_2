
S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))
D = (S/2)**2 - P
if D > 0:
    X1 = S/2 + D**0.5
    X2 = S/2 - D**0.5
    if (int(X1) == X1 and int(X2) == X2):
        print(f"{int(X1)} и {int(X2)}")
    else:
        print("Задуманные числа не целые")
else:
    print("Невозможно вычислить")