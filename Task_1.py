int_list = []
for i in input("Введите последовательность монет: ").split():
    int_list.append(int(i))
zero = 0
first = 0
for i in int_list:
    if i == 0:
        zero += 1
    elif i == 1:
        first += 1
if zero > first:
    print(first)
elif first > zero:
    print(zero)
else:
    print(zero)
