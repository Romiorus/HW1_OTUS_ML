# Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря. Написать вторую функцию,
# которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'


def caesar_cipher(word, key):
    # Проверяем, является ли ключ допустимым
    # if not isinstance(key, int) or key < 0 or key > 26:
    # raise ValueError('Ключ должен быть целым числом от 0 до 26')

    # Проверяем, является ли слово допустимым
    if not isinstance(word, str):
        raise ValueError('Слово должно быть строкой')

    # Шифруем слово
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in word:
        if char in alphabet:
            index = alphabet.find(char)
            result += alphabet[(index + key) % 26]
        else:
            result += char
    return result


print('шифр слова "dog" ключ 3:', caesar_cipher('dog', 3))
print('шифр слова "python" ключ 5:', caesar_cipher('python', 5))
print('дешифр слова "grj" ключ 3:', caesar_cipher('grj', -3))
print('дешифр слова "udymts" ключ 5:', caesar_cipher('udymts', -5))
