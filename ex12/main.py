# В лабе требуется описание только одной функции на выбор. Здесь их с запасом.
# 1. Функция sin(x):

import math

# Начало и конец интервала
A = 0
B = 10
# Шаг
H = 1

# Функция для табулирования


def f(x):
    return math.sin(x)


# Табулирование функции
for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")

"""
# 2. Функция cos(x):

def f(x):
    return math.cos(x)


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")


# 3. Функция tan(x):

def f(x):
    return math.tan(x)


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")


# 4. Функция exp(x):

def f(x):
    return math.exp(x)


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")


# 5. Функция sqrt(x):

def f(x):
    return math.sqrt(x)


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")


# 6. Функция x^2:

def f(x):
    return x**2


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")


# 7. Функция x^3:

def f(x):
    return x**3


for i in range(A, B+1, H):
    print(f"x = {i}, f(x) = {f(i):.2f}")

"""
