import string
import random

availability_uppercase = bool(int(input('Наличие верхнего регистра (1/0 True/False): ')))
availability_lowercase = bool(int(input('Наличие нижнего регистра (1/0 True/False): ')))
availability_special_characters = bool(int(input('Наличие спец символов (1/0 True/False): ')))
availability_numbers = bool(int(input('Наличие цифр (1/0 True/False): ')))
len_password = int(input('Длина пароля: '))


def generator(availability_uppercase, availability_lowercase, availability_special_characters, availability_numbers,
              len_password):
    alf_uppercase = string.ascii_uppercase if availability_uppercase else ''
    alf_lowercase = string.ascii_lowercase if availability_lowercase else ''
    special_characters = '!@#$%^&*<>' if availability_special_characters else ''
    numbers = '1234567890' if availability_numbers else ''

    number_of_check_marks = availability_uppercase + availability_lowercase + availability_special_characters + availability_numbers
    allowed_characters = alf_uppercase + alf_lowercase + special_characters + numbers
    password = ''

    if number_of_check_marks == 0:
        return 'Не выбран ни один пункт'
    if len_password < number_of_check_marks:
        return 'Длина пароля меньше количества выбранных пунктов'

    password += random.choice(alf_uppercase) if availability_uppercase else ''
    password += random.choice(alf_lowercase) if availability_lowercase else ''
    password += random.choice(special_characters) if availability_special_characters else ''
    password += random.choice(numbers) if availability_numbers else ''

    while len_password != len(password):
        password += random.choice(allowed_characters)

    return password


print(generator(availability_uppercase, availability_lowercase, availability_special_characters, availability_numbers,
                len_password))
