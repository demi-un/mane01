import string

text = input('текст: ')
bias = int(input('смещение: '))


def language_recognizer(text: str):
    RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ENG = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

    for i in text:
        if i in RUS:
            return RUS
        elif i in ENG:
            return ENG


def encryption(text, bias):
    language = language_recognizer(text)
    res = ''
    for i in text:
        if i == ' ':
            res += ' '
        else:
            res += language[language.index(i) + bias]
    return res


print(f'Зашифрованное сообщение: {encryption(text, bias)}')
