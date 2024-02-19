# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой)
# и возвращает его корни, либо сообщает, что их нет
# "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7


def solve_quadratic_equation(equation):
    # Извлекаем коэффициенты из уравнения
    coefficients = equation.split(' ')
    if len(coefficients) == 7:
        # Ищем позицию символа 'x' в элементах списка
        coefficient_list = []
        for i in range(len(coefficients)):
            x_index = coefficients[i].find('x')
            # Если символ 'x' найден, проверяем символы перед ним
            if x_index != -1:
                # Инициализируем переменную для коэффициента
                coefficient = ''
                string = coefficients[i]
                # Начинаем цикл с символа перед 'x' и идем в обратном направлении
                j = x_index - 1
                while j >= 0:
                    # Если символ является числом или знаком '-', добавляем его в переменную коэффициента
                    if string[j].isdigit() or string[j] == '-':
                        coefficient = string[j] + coefficient
                        j -= 1
                    # Если символ является '*', идем дальше
                    elif string[j] == '*':
                        j -= 1
                    # Если символ не является числом, '*' или '-', значит коэффициент равен 1
                    else:
                        coefficient = "1"
                        break
                # Если переменная коэффициента пустая, значит коэфф 1, иначе приводим ее к инт
                if coefficient == '':
                    coefficient = 1
                elif coefficient == '-':
                    coefficient = -1
                else:
                    coefficient = int(coefficient)
                coefficient_list.append(coefficient)  # добавили найденный коэфф с список

        a = coefficient_list[0]
        if coefficients[1] != '-':
            b = coefficient_list[1]
        else:
            b = -coefficient_list[1]
        if coefficients[3] != '-':  # "c" коэфф не содержит 'x' выдергиваем его из начального выражения.
            c = int(coefficients[4])
        else:
            c = -int(coefficients[4])

        # Вычисляем дискриминант
        discriminant = b ** 2 - 4 * a * c

        # Проверяем значение дискриминанта
        if discriminant > 0:
            # Вычисляем корни
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            return f'Найдено два корня: x_1 = {x1}, x_2 = {x2}'
        elif discriminant == 0:
            # Единственный корень
            x = -b / (2 * a)
            return f'Найден единственный корень x = {x}'
        else:
            # Корней нет
            return 'Дискрименант отрицательный, корней нет'
    else:
        return ('Неверный формат уравнения, введите в формате "a*x**2 + b*x + c = 0",'
                'если какой либо коэффициент отсутствует, указать его как "0", например: x**2 + 0*x - 36 = 0')


print('Дано: "x**2 - 11*x + 28 = 0"')
print(solve_quadratic_equation("x**2 - 11*x + 28 = 0"))
