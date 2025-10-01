# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские
# Работает только конвертация из арабских цифр в римские

print('''<--------------------------->
- Допускаются лишние символы-разделители (кавычки, квадратные скобки, запятые, пробелы).
- Можно вводить как римские, так и арабские числа одновременно.
- Допускаются натуральные и/или римские числа

примеры входных данных: 
["IV", "1", "XLII", "12", "MMXXIII"]
[IV, IX, XLII, XCIX, MMXXIII]
IX
XLII, XCIX
"XCIX", "MMXXIII"
<--------------------------->''')

# вставить число/числа в переменную data, если нужно внести данные без терминала (list / str / int)
data = input('введите числа: ')


# преобразование строки / числа в список
def data_transformation(numbers):
    if type(numbers) == str:
        while '[' in numbers: numbers = numbers.replace('[', ' ')
        while ']' in numbers: numbers = numbers.replace(']', ' ')
        while '"' in numbers: numbers = numbers.replace('"', ' ')
        while "'" in numbers: numbers = numbers.replace("'", ' ')
        while ',' in numbers: numbers = numbers.replace(',', ' ')
        numbers = numbers.split()
    elif type(numbers) == int:
        numbers = list(numbers)

    return numbers


data = data_transformation(data)


numerals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
(10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
(1, "I")]


# определитель арабских / римских чисел
def determinant(number):
    if type(number) == int:
        number = str(number)
    if any(ch in number for ch in "IVXLCDM"):
        return 'rim'
    else:
        return 'arab'


# возвращает True, если числа взяты из одного языка (например, только арабские числа), иначе False
def number_of_different_languages(lst):
    list_language = []
    for el in lst:
        if len(list_language) > 1:
            return False

        if determinant(el) not in list_language:
            list_language.append(determinant(el))

    return True


# в какой язык конвертировать числа
if not number_of_different_languages(data):
    final_language = input('В какой язык конвертировать числа (rim / arab): ')
else:
    final_language = 'arab' if determinant(data[0]) == 'rim' else 'rim'


def converter(numbers, end_language):
    res = []

    for number in numbers:
        if end_language == determinant(number):
            res.append(number)
            continue

        if end_language == 'rim':
            res.append('')
            number = int(number)

            counter = 0
            while number > 0:
                while number - numerals[counter][0] >= 0:
                    res[-1] += numerals[counter][1]
                    number = number - numerals[counter][0]
                counter += 1

    return res


print(converter(data, final_language))
