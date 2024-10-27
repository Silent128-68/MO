# import numpy as np
# def f(x):
#     return (x + 2) * (x + 1) * (x - 1) * (x - 0.5) - 1
# # Оценка константы Липшица L, контролирующей максимальный наклон ломаных
# L = 15  # Примерное значение; точное значение можно уточнить
#
# # Задаем границы интервала, на котором ищем минимум
# a, b = -2, 2
#
# # Вычисляем координаты начальной точки пересечения ломаных x0 и y0
# # x0 и y0 задают начальную точку для первой аппроксимации p0(x)
# x0 = (f(a) - f(b) + L * (a + b)) / (2 * L)
# y0 = (f(a) + f(b) + L * (a - b)) / 2
#
# # Определяем начальную кусочно-линейную функцию p0(x) на основе f(a) и f(b)
# # p0(x) - это ломаная, задающая начальную аппроксимацию функции f(x) на интервале [a, b]
# def p0(x):
#     if x <= x0:
#         return f(a) - L * (x - a)
#     else:
#         return f(b) + L * (x - b)
#
# # Определяем вспомогательную функцию pk(x), используемую для построения ломаных на каждом шаге
# def pk(x, xk_prev, pk_prev):
#     # g(x) = f(xk_prev) - L * |x - xk_prev|
#     g_val = f(xk_prev) - L * np.abs(x - xk_prev)
#     return max(pk_prev(x), g_val)  # максимум между предыдущей аппроксимацией и g(x)
#
# # Основная функция метода ломаных для поиска минимума
# def broken_lines_method(tol=1e-5, max_iter=100):
#     xk = x0  # начальная точка минимума
#     pk_prev = p0  # начальная функция ломаной p0(x)
#
#     # Итерационный процесс для приближения к минимуму
#     for k in range(max_iter):
#         # Находим расстояние ∆ для поиска новых точек минимума
#         delta = (f(xk) - pk_prev(xk)) / (2 * L)  # шаг, равный половине разницы между f и pk
#
#         # Определяем новые точки минимума на текущем шаге
#         xk_new_left = xk - delta
#         xk_new_right = xk + delta
#
#         # Вычисляем значения ломаной функции в новых точках
#         pk_left = pk(xk_new_left, xk, pk_prev)
#         pk_right = pk(xk_new_right, xk, pk_prev)
#
#         # Определяем, какая из новых точек дает меньшее значение функции ломаной
#         if pk_left < pk_right:
#             xk_next, pk_next = xk_new_left, pk_left
#         else:
#             xk_next, pk_next = xk_new_right, pk_right
#
#         # Проверяем условие окончания: если разница между f(x) и pk(x) меньше заданной точности, то останавливаем
#         if abs(f(xk_next) - pk_next) < tol:
#             return xk_next, f(xk_next)
#
#         # Обновляем значения для следующей итерации
#         xk = xk_next  # новая точка минимума
#         pk_prev = lambda x: pk(x, xk, pk_prev)  # обновляем аппроксимацию ломаной
#
#     # Если достигнуто максимальное количество итераций, возвращаем последнее найденное значение
#     return xk, f(xk)
#
# xmin, fmin = broken_lines_method()
# print(f"Минимум функции f(x) ≈ {fmin} достигается при x ≈ {xmin}")

import numpy as np


# Функция f(x), которую минимизируем
def f(x):
    return (x + 2) * (x + 1) * (x - 1) * (x - 0.5) - 1


# Производная функции f(x) для оценки коэффициента Липшица
def df(x):
    return 4 * x ** 3 - 3.5 * x ** 2 - 1.5 * x + 0.5


# Вспомогательная функция g, зависящая от фиксированной точки x_bar и параметра L
def g(x_bar, x, L):
    return f(x_bar) - L * np.abs(x - x_bar)


# Основной метод ломаных для нахождения минимума
def broken_lines_method(a=-2, b=2, epsilon=1e-6, max_iter=100):
    # Оценка коэффициента Липшица L на интервале [a, b]
    x_vals = np.linspace(a, b, 100)
    L = max(np.abs(df(x_vals)))  # максимальное значение производной на интервале

    # Инициализация начальных значений
    xk = (a + b) / 2  # начальная точка
    pk_prev_values = {x: g(xk, x, L) for x in x_vals}  # начальная аппроксимация на сетке
    iteration = 0

    while iteration < max_iter:
        # Определение текущей аппроксимации pk на основе предыдущих значений
        pk = lambda x: max(pk_prev_values.get(x, g(xk, x, L)), g(xk, x, L))

        # Вычисляем новое значение шага delta, согласно алгоритму
        delta = (f(xk) - pk(xk)) / (2 * L)

        # Обновляем значения xk_left и xk_right
        xk_left = xk - delta
        xk_right = xk + delta

        # Проверяем, чтобы точки xk_left и xk_right оставались в пределах [a, b]
        xk_left = max(a, xk_left)
        xk_right = min(b, xk_right)

        # Вычисляем значения функции в новых точках
        f_left = f(xk_left)
        f_right = f(xk_right)

        # Обновляем точку xk в зависимости от значений f_left и f_right
        if f_left < f_right:
            xk = xk_left
        else:
            xk = xk_right

        # Добавляем текущие значения pk в словарь аппроксимации
        pk_prev_values[xk_left] = pk(xk_left)
        pk_prev_values[xk_right] = pk(xk_right)

        # Проверка на условие остановки
        if abs(f(xk) - pk(xk)) < epsilon:
            break

        # Вывод текущей информации о минимуме на каждом шаге
        print(f"Итерация {iteration + 1}: xk = {xk}, f(xk) = {f(xk)}, pk(xk) = {pk(xk)}")

        iteration += 1

    return xk, f(xk)


# Запуск алгоритма
xmin, fmin = broken_lines_method()
print("Минимум функции достигается в точке x =", xmin)
print("Значение функции в этой точке f(x) =", fmin)
