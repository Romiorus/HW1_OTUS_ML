# БЕсплатный пайчарм не редактирует юпитер
# по совету препода перевел все в питонячиЙ файл
# Задача 1
task = ("""N хоббитов делят K кусков эльфийского хлеба поровну
не делящийся нацело остаток остается в корзинке у Сэма.
Напишите функцию, которая принимает на вход параметры) N и K
и возвращает два числа: x - cколько кусков эльфиского хлеба достанется каждому хоббиту,
и y - сколько кусков остаётся в корзинке.""")


def share_bread(N, K):
    x = K // N
    y = K % N
    print(x, y)
    return x, y


# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
print("задача 1:")
print(task)
print("ответ при заданных N=3, K=14:")
assert share_bread(N=3, K=14) == (4, 2)

# Задача 2
task = ("""В копях Мории хоббиты нашли стену, на которой высечены разные натуральные числа. 
Согласно древним сказаниям, это даты сражений. Хоббиты знают, 
что сражения происходили только по високосным годам. 
Помогите хоббитам определить, является ли год с данным числом датой великого сражения. 
Если это так, то верните строку "YOU SHALL PASS", иначе верните "YOU SHALL NOT PASS". 
Напомним, что в соответствии с хоббитским календарем, год является високосным, 
если его номер кратен 4, но не кратен 100, а также если он кратен 400""")


def leap_year(year):
    text_result = ""
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        text_result = 'YOU SHALL PASS'
    else:
        text_result = "YOU SHALL NOT PASS"
    return text_result


print("задача 2:")
print(task)
print()
print("ответ при заданной дате сражения '500'")
print(leap_year(500))

# Задача 3
import math


def amulet_area(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt((p * ((p - a) * (p - b) * (p - c))))
    return S


print(amulet_area(3, 4, 5))

# Задача 4
import numpy as np


def cal_euclidean(a, b):
    distance = np.sqrt(np.sum(np.square(a - b)))
    ## Your code here
    return distance


def cal_manhattan(a, b):
    distance = np.sum(np.absolute(a - b))
    ## Your code here
    return distance


def cal_cosine(a, b):
    distance = 1 - ((np.sum(a * b)) / ((np.linalg.norm(a)) * (np.linalg.norm(b))))
    ## Your code here
    return distance


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))

# Задача 5
my_array = np.random.rand(100)
print(np.max(my_array), np.min(my_array))
index_max = np.where(my_array == np.max(my_array))
index_min = np.where(my_array == np.min(my_array))
my_array[index_max] = 1
my_array[index_min] = 0
print(my_array)

# Создайте array размером 5 × 6
# с целыми числами в интервале [0,50].
# Напечатайте колонку, которая содержит
# максимальный элемент полученной матрицы

my_array = np.random.randint(0, 50, size=(5, 6))
index = np.where(np.max(my_array) == my_array)
selected_column = index[1]
print(my_array[:, index[1]])

print('Shape: ', my_array.shape)
print('Array')
print(my_array)
print(selected_column)


# Напишите функцию, которая принимает на вохд
# матрицу (array) X и возвращает все её уникальные строки
# в виде новой матрицы.

def get_unique_rows(X):
    X_unique = np.unique(X, axis=0)
    return X_unique


X = np.random.randint(4, 6, size=(10, 3))
print(X)

get_unique_rows(X)
