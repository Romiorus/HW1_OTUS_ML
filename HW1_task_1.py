# первый варинат через простейшие операторы цикла
# Вводится целое число (любого размера).
# Написать функцию, которая разобьет это число на разряды символом "пробел", Функция возвращает тип данных str
# Например: 1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`
def split_number(num):
    if num <= 999:
        return (str(num))
    elif len(str(num)) % 3 == 2:
        result = str(num)[0:2] + ' '
        for i in range(2, len(str(num)), 3):
            result += str(num)[i:i + 3]
            result += ' '
    elif len(str(num)) % 3 == 1:
        result = str(num)[0:1] + ' '
        for i in range(1, len(str(num)), 3):
            result += str(num)[i:i + 3]
            result += ' '
    else:
        result = ''
        for i in range(0, len(str(num)), 3):
            result += str(num)[i:i + 3]
            result += ' '
    result = result[:-1]  # удаляем последний пробел
    return (result)


print(split_number(100))
print(split_number(1000))
print(split_number(10000))
print(split_number(100000))
