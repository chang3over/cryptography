import re
import pandas as pd
import random


def clean_text(input_text, output_text):
    with open(input_text, encoding="utf-8") as book:
        with open(output_text, "w", encoding="utf-8") as text:
            for i in book:
                text.write(re.sub(r'[.,"\'-?:!;–?\n«»…óáéegros№“—abcdfhijklmnpqtuvwxyzê„ ]', '', i).lower())


def analiz(text, book_excel):
    b = {}
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    with open(text, encoding="utf-8") as book:
        for i in book.read():
            if i.lower() in alphabet:
                try:
                    b[i][0] += 1
                except:
                    b[i] = [1]
    a = []
    for i in b:
        if i in alphabet:
            a.append([i, b[i]])
    a.sort()
    b.clear()
    for i in a:
        b[i[0]] = i[1]
    df = pd.DataFrame(b)
    df.to_excel(book_excel)


a = [1, 2, 3]

random.shuffle(a)
print(a)