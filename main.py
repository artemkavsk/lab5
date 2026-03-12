import re


# task1

text = open('task1-ru.txt', encoding='utf-8').read()

# слова 3-5 букв
print(re.findall(r'\b[а-яё]{3,5}\b', text, flags=re.I))

# числа больше 3 знаков
print(re.findall(r'\b\d{4,}\b', text))


# task2

html = open('task2.html', encoding='utf-8').read()

# все открывающие теги
tags = re.findall(r'<([a-zA-Z0-9]+)', html)

# без повторений
print(set(tags))