# Написать функцию, которая заменяет строку текста и изменяет снейк_кейс на КамелКейс и наоборот
# my_first_func -> MyFirstFunc, AnotherFunction -> another_function
def convert_case(input_string):
    if '_' in input_string:
        # снейк_кейс на КамелКейс
        parts = input_string.split('_')
        capitalized_parts = [part.capitalize() for part in parts]
        return ''.join(capitalized_parts)
    else:
        # КамелКейс в снейк_кейс
        result = ''
        # enumerate возвращает индекс и символ для каждого символа в строке
        for index, char in enumerate(input_string):
            # проверяем, является ли текущий символ заглавной буквой и не является ли он первым символом в строке
            if char.isupper() and index != 0:
                result += '_' + char.lower()
            else:
                result += char.lower()  # добавить первый символ в нижнем регистре если он есть.
        return result


print('Было: "my_first_func", стало:', convert_case('my_first_func'))
print('Было: "AnotherFunction", стало:', convert_case('AnotherFunction'))
