import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def root(a, b):
    b = pow(b, -1)
    return pow(a, b)



ops = {'+': add, '-': sub, '*': mul, '/': div, '^': pow, 'l': math.log, 'r': root}

def first_calc(inpt):
    flag = 0
    cnt = 0
    for i in range(len(inpt)):
        if inpt[i] in ops:                      # это нам необходимо для проверки на минус
            if inpt[i] == '-' and cnt > 0:      # ведь могут вводиться отрицательные числа
                continue
            flag = i
            cnt += 1
            
    

    if flag == 0:       # смотрим попадался ли нам оператор
        print("Не было встречено оператора (либо вы ввели первым символом оператора и только одно число)")
        return
    elif flag != 0 and cnt > 1:     # если встретилось больше одного оператора в строке
        print("Введено более одного оператора")
        return
    else:
        op = inpt[flag]
        # попытка преобразовать первое число 
        try:
            float(inpt[:flag])
        except ValueError:
            print(f"Невозможно преобразовать первое число {inpt[:flag]}, похоже, это и не число. Завершаю программу")
            exit()
        else:
            first = float(inpt[:flag])
        
        # попытка преобразовать второе число
        try:
            float(inpt[flag+1:])
        except ValueError:
            print(f"Невозможно преобразовать второе число {inpt[flag+1:]}, похоже, это и не число. Завершаю программу")
            exit()
        else:
            second = float(inpt[flag+1:])

        # print(f"Первое число: {first}")
        # print(f"Второе число: {second}")
        # print(f"Оператор: {inpt[flag]}")

        # если у нас логарифм, то его основание должно быть положительным
        if op == 'l' and second < 0:
            print("Логарифм не может быть с отрицательным основанием, преобразовываю в положительное")
            second = abs(second)
        if op == 'l' and first < 0:
            print(f"Логарифм должен браться от положительного числа(сейчас от {first}). Возвращаю единицу")
            return 1
        try:
            ops[op](first, second)
        except ZeroDivisionError:
            res = math.nan
        except OverflowError:
            res = math.inf
        else:
            res = ops[inpt[flag]](first, second)
        
        return res

def cont_calc(prev, new):
    # получаем оператора и число
    if new[0] not in ops:
        print(f"Похоже, первый символ {new[0]} это не оператор, операция отменяется")
        return
    else:
        op = new[0]
        nmbr = new[1:]
    
    # пытаемся преобразовать число для работы с ним
    try:
        float(nmbr)
    except ValueError:
        print(f"Невозможно преобразовать число {nmbr}, похоже, это и не число. Возвращаю исходное значение")
        return prev
    else:
        nmbr = float(nmbr)

    if op == 'l' and nmbr < 0:
        print(f"Логарифм не может быть с отрицательным основанием({nmbr}), преобразовываю в положительное")
        nmbr = abs(nmbr)
    if op == 'l' and prev < 0:
        print(f"Логарифм должен браться от положительного числа(сейчас от {prev}). ничего не выполняю")
        return prev
    try:
        ops[op](prev, nmbr)
    except ZeroDivisionError:
        res = math.nan
    except OverflowError:
        res = math.inf
    else:
        res = ops[op](prev, nmbr)

    return res


print("""Калькулятор

Для сложения используется оператор                                  +       (5+10)
Для вычетания используется оператор                                 -       (27-8)
Для деления используется оператор                                   /       (32/4)
Для умножения используется оператор                                 *       (2*4)
Для возведения в степень используется оператор                      ^       (16^2)
Для нахождения корня n-ой степени используется оператор             r       (36r2)
Для нахождения логарифма по основанию n используется оператор       l       (1024l2)
Для выхода нажмите                                                  Enter

Формат ввода: 5+10 - пример начального вычисления
              ^100 - пример последующего вычисления 
              -325 - пример последующего вычисления\n""")

inpt = input("Пожалуйста, введите начальное вычисление (например 20+7): ")

if inpt == '':
        print("\nВыход из программы\n")
        exit()
else:
    res = first_calc(inpt)
    while 1:
        print(f"Результат: {res}\n")
        inpt = input("Продолжаем считать?(Выход - Enter): ")

        if inpt == '':
            print("\nВыход из программы\n")
            exit()
        else:
            res = cont_calc(res, inpt)
