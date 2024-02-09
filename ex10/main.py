import math


def solve_quadratic(a, b, c):
    # Вычисляем дискриминант
    D = (b**2) - (4*a*c)

    # Проверяем, что дискриминант неотрицательный
    if D < 0:
        print("Уравнение не имеет действительных корней")
        return None

    # Вычисляем два корня
    root1 = (-b-math.sqrt(D))/(2*a)
    root2 = (-b+math.sqrt(D))/(2*a)

    return (root1, root2)


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic(a, b, c)

if roots is not None:
    print("Корни квадратного уравнения: ", roots)
