### вычисление с помощью функции
def fact(n):
    if n == 0:
        return 1            # 0! = 1
    elif n < 0:
        return -1
    else:
        res = 1
        for i in range(1, n+1):         # здесь необходимо идти от 1 до n+1, так как иначе первым множителем будет 0
                                        # что приведет к обнулению результата
            res = res * i
        return res


while 1:
    nmbr = input("\nПожалуйста, введите число для посчета факториала, либо Enter для выхода: ")
    print()

    if nmbr == '':
        print("Завершение программы")
        exit()
    try:
        int(nmbr)
    except ValueError:
        print(f"\nПохоже, Вы ввели не число, а {nmbr}")
    else:
        # перевод строки ввода в число
        n = int(nmbr)
        print(f"\nВы ввели число {n}\n")
        
        ### анонимная функция для посчета факториала без рекурсии
        reduce = lambda n: n-1
        res = 1
        i = n
        while reduce(i):
            res = res * i
            i = reduce(i)
        
        ### анонимная функция для посчета факториала с рекурсией
        fact_recurs = lambda n: n * fact_recurs(n-1) if n > 0 else 1

        print(f"При подсчете через функцию без рекурсии результат: {fact(n)}")
        print(f"При подсчете через анонимную функцию без рекурсии результат: {res}")
        print(f"При подсчете через анонимную функцию с рекурсией результат: {fact_recurs(n)}")
    