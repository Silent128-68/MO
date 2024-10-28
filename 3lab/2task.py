def f(x):
    return (x + 2) * (x + 1) * (x - 1) * (x - 0.5) - 1
# Вычисление вспомогательной функции g(x), зависящей от точки x0 и константы Липшица L
def g(x, x0, L):
    return f(x0) - L * abs(x - x0)
# Нахождение точки пересечения между функциями на интервале [left, right] с заданным значением L
def intersection(left, right, L):
    return (f(left) - f(right) + L * (left + right)) / (2 * L)
# Метод ломаных для минимизации функции f на заданном интервале
def broken_lines_method(tol=1e-5):
    left, right = -2, 2
    L = 15  # Примерное значение константы Липшица

    # Инициализируем точки для аппроксимации ломаной
    points = [(left, f(left))]  # Левая граница
    x0 = intersection(left, right, L)  # Вычисляем начальную точку пересечения x0
    points.append((x0, g(x0, left, L)))  # Добавляем эту точку и её значение g(x)
    points.append((right, f(right)))  # Правая граница

    while True:
        # Ищем точку с минимальным значением y среди внутренних точек
        min_index = 1
        for i in range(1, len(points), 2):
            if points[i][1] < points[min_index][1]:
                min_index = i

        # Обновляем значение функции в точке минимума
        x_min = points[min_index][0]
        y_min = points[min_index][1]
        points[min_index] = (x_min, f(x_min))

        # Находим новые точки пересечения и добавляем их в ломаную
        left_intersection = intersection(points[min_index - 1][0], x_min, L)
        right_intersection = intersection(x_min, points[min_index + 1][0], L)

        # Добавляем новые точки пересечения в список точек ломаной
        points.insert(min_index, (left_intersection, g(left_intersection, x_min, L)))
        points.insert(min_index + 2, (right_intersection, g(right_intersection, x_min, L)))

        # Условие остановки по точности
        if abs(f(x_min) - y_min) < tol:
            return x_min, f(x_min)

xmin, fmin = broken_lines_method()
print(f"Минимум функции f(x) ≈ {fmin} достигается при x ≈ {xmin}")
