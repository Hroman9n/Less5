import re                   # regex необходим для посчета предложений

### функция для посчета частоты символов
def sym_freq(text):

    symbols = {}

    for i in text:
        if i in symbols:
            symbols[i] += 1
        else:
            symbols[i] = 1

    for i in symbols:
        if i == '\n':
            print(f"Символ переноса строки встречается {symbols[i]} раз")
        elif i == ' ':
            print(f"Пробел встречается {symbols[i]} раз")
        else:
            print(f'Символ "{i}" встречается {symbols[i]} раз')


### функция для посчета количества слов
def words_freq(text):

    words = {}

    # заменяем все знаки пунктуации на пробелы
    for i in '.,!':
        text = text.replace(i, ' ')
    text.lower()

    # с помощью сплита разделяем и получаем список из слов
    text_list = text.split()

    #                       длинна списка
    print(f"В данном тексте {len(text_list)} слов") 

### подсчет количества предложений
def sent_freq(text):
    #     здесь мы используем regex для поиска знаков пунктуации, по которым и разделяем предложения
    res = re.split(r'[.!?]+', text)
    
    # так как в итоге мы получаем список, в котором последним элементом является '' (я так и не понял почему), то мы уменьшаем количество на 1
    print(f"В данном тексте {len(res)-1} предложений")

test_text = """Hi! Nice to meet you!
My name is John Smith. I am 19 and a student in college.
I go to college in New York. 
My favorite courses are Geometry, French, and History. 
English is my hardest course. My professors are very friendly and smart.
It’s my second year in college now. I love it!
I live in a big house on Ivy Street. It’s near the college campus.
I share the house with three other students. Their names are Bill, Tony, and Paul.
We help each other with homework. On the weekend, we play football together.
I have a younger brother. 
He just started high school. He is 14 and lives with my parents. 
They live on Mulberry Street in Boston. Sometimes they visit me in New York. 
I am happy when they visit. My Mom always brings me sweets and candy when they come. 
I really miss them, too!"""

while 1:
    print("""\nПодсчет частоты символов/количества слов/количества предложений
    Для подсчета частоты символов введите           1
    Для подсчета количества слов введите            2
    Для подсчета количества предложений введите     3
    Для выхода нажмите                              Enter""")

    ask = input("Выбор функции: ")

    if ask == '':
        print("Завершение программы")
        exit()
    elif ask == '1':
        ask2 = input("Введите свой текст, либо нажмите Enter для ввода заранее написанного текста: ")
        if ask2 == '':
            sym_freq(test_text)
        else:
            sym_freq(ask2)
    elif ask == '2':
        ask2 = input("Введите свой текст, либо нажмите Enter для ввода заранее написанного текста: ")
        if ask2 == '':
            words_freq(test_text)
        else:
            words_freq(ask2)
    elif ask == '3':
        ask2 = input("Введите свой текст, либо нажмите Enter для ввода заранее написанного текста: ")
        if ask2 == '':
            sent_freq(test_text)
        else:
            sent_freq(ask2)
    else:
        print(f"Похоже, вы ввели {ask}, попробуйте ещё раз")