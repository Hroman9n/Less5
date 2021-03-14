def counting(text):

    symbols = {}

    for i in text:
        cnt = lambda i: symbols[i]+1 if i in symbols else 1
        symbols[i] = cnt(i)
    
    for i in symbols:
        if i == '\n':
            print(f"Символ переноса строки встречается {symbols[i]} раз")
        elif i == ' ':
            print(f"Пробел встречается {symbols[i]} раз")
        else:
            print(f'Символ "{i}" встречается {symbols[i]} раз')

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

text = input("Введите свой текст, либо нажмите enter для подсчета символов в заранее готовом тексте: ")

if text == "":
    counting(test_text)
else:
    counting(text)