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
        if inpt[i] in ops:
            flag = i
            cnt += 1
    

    if flag == 0:       # смотрим попадался ли нам оператор
        print("Не было встречено оператора (либо вы ввели первым символом оператора и только одно число)")
        return
    elif flag != 0 and cnt > 1:     # если встретилось больше одного оператора в строке
        print("Введено более одного оператора")
        return
    else:
        # попытка преобразовать первое число 
        try:
            float(inpt[:flag])
        except ValueError:
            print(f"Невозможно преобразовать первое число {inpt[:flag]}, похоже, это и не число")
            return
        else:
            first = float(inpt[:flag])
        
        # попытка преобразовать второе число
        try:
            float(inpt[flag+1:])
        except ValueError:
            print(f"Невозможно преобразовать второе число {inpt[flag+1:]}, похоже, это и не число")
            return
        else:
            second = float(inpt[flag+1:])

        # print(f"Первое число: {first}")
        # print(f"Второе число: {second}")
        # print(f"Оператор: {inpt[flag]}")

        try:
            ops[inpt[flag]](first, second)
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
        print(f"Невозможно преобразовать число {nmbr}, похоже, это и не число")
        return
    else:
        nmbr = float(nmbr)

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

Для сложения используется оператор                                  +
Для вычетания используется оператор                                 -
Для деления используется оператор                                   /
Для умножения используется оператор                                 *
Для возведения в степень используется оператор                      ^
Для нахождения корня n-ой степени используется оператор             r
Для нахождения логарифма по основанию n используется оператор       l
Для выхода нажмите                                                  Enter

Формат ввода: 5+10 - пример начального вычисления
              ^100 - пример последующего вычисления 
              -325 - пример последующего вычисления\n""")

init = input("Пожалуйста, введите начальное вычисление (например 20+7): ")

if init == '':
    print("\nВыход из программы\n")
else:
    a = first_calc(init)
    print(a)
