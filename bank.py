# Функция для расчета одноразового взноса
def bank(sum, m, p):

    for i in range(m):
        sum *= 1 + (p/100)

    return sum

# Функция для расчета повторяемых ежемесечно взносов
def bank_rep(sum, m, p):

    total = sum
    for i in range(m):
        total += sum
        total *= 1 + (p/100)

    return total


while 1:
    print("""Расчет накопительного счета
    Для расчета при одноразовом взносе наберите         1
    Для расчета при ежемесячных взносах нажмите         2
    Для выхода нажмите                                  Enter\n""")

    ask = input("Вариант ввода: ")

    if ask == '':
        print("Завершаю программу")
        exit()
    else:
        sum = input("Введите планируемый взнос: ")
        m = input("Введите планируемый срок платежа: ")
        p = input("Введите процент (например, 15): ")

    try:
        float(sum)
    except ValueError:
        print(f"Невозможно преобразовать {sum} в число")
    else:
        sum = float(sum)

    try:
        int(m)
    except ValueError:
        print(f"Невозможно преобразовать {m} в число")
    else:
        m = int(m)
    
    try:
        float(p)
    except ValueError:
        print(f"Невозможно преобразовать {p} в число")
    else:
        p = float(p)

    if ask == '1':
        res = bank(sum, m, p)
    elif ask == '2':
        res = bank_rep(sum, m, p)
    
    print(f"\nЗа {m} месяцев вы бы скопили {res:.3f} валюты\n")
