counter_attempts = 0
hidden_word = input('Загадайте слово: ')

hidden_word_dict = {hidden_word[i]: False for i in range(len(hidden_word))}
guessed_letters = ''.join('_' for i in range(len(hidden_word)))
list_of_written_letters = ''

ascii_arts = [
    """
          ________
         |        |
         |
         |
         |
         |
        ---
    """,
    """
          ________
         |        |
         |        O
         |
         |
         |
        ---
    """,
    """
          ________
         |        |
         |        O
         |        |
         |
         |
        ---
    """,
    """
          ________
         |        |
         |        O
         |       /|
         |
         |
        ---
    """,
    """
          ________
         |        |
         |        O
         |       /|\\
         |
         |
        --- 
    """,
    """
          ________
         |        |
         |        O
         |       /|\\
         |       /
         |
        ---
    """,
    """
          ________
         |        |
         |        O
         |       /|\\
         |       / \\
         |
        ---
    """
]


def letter_check(char: str, word: str):
    return word.find(char)


def print_info(text):
    print('\n'*100 + f'<--------------{text}--------------------->')
    print(ascii_arts[counter_attempts])
    print('')
    print(f'угаданные буквы: {guessed_letters}')


message = ''
while True:
    if counter_attempts >= 6:
        print_info('Вы не смогли угадать слово')
        break
    if '_' not in guessed_letters:
        print_info('Вы отгадали слово')
        break

    print_info(message)

    letter = input('Введите букву: ')

    if len(letter) != 1 or not letter.isalpha():
        message = 'Неверный ввод'
        continue
    if letter in list_of_written_letters:
        message = 'Вы уже вводили эту букву'
        continue

    list_of_written_letters += letter

    if letter_check(letter, hidden_word) == -1:
        counter_attempts += 1
        message = 'Буква не угадана'
        continue

    message =  'Вы угадали букву'
    for i in range(hidden_word.count(letter)):
        index_of_the_guessed_letter = letter_check(letter, hidden_word)
        guessed_letters = guessed_letters[:index_of_the_guessed_letter] + letter + guessed_letters[
            index_of_the_guessed_letter + 1:]
        hidden_word = hidden_word.replace(letter, ' ', 1)
