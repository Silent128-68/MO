def f(x):
    return x ** 3 + 2 * x ** 2 + x
def df(x):
    return 3 * x ** 2 + 4 * x + 1
def midpoint_method(a, b, epsilon=1e-6):
    while (b - a) / 2 > epsilon:  # Шаг 1: Вычисляем среднюю точку x̄ и производную в точке x̄
        x_mid = (a + b) / 2
        df_mid = df(x_mid)

        if abs(df_mid) <= epsilon:  # Шаг 2: Проверяем, близка ли производная к нулю
            x_min = x_mid  # Если производная близка к нулю, то найден минимум
            f_min = f(x_mid)
            return x_min, f_min

        if df_mid > 0:  # Шаг 3: Обновляем отрезок в зависимости от знака производной
            b = x_mid  # Сдвигаем верхнюю границу к x_mid
        else:
            a = x_mid  # Сдвигаем нижнюю границу к x_mid
    # После цикла возвращаем среднюю точку как лучший приближенный минимум
    x_min = (a + b) / 2
    f_min = f(x_min)
    return x_min, f_min

a = -0.9
b = 0.5
epsilon = 1e-6

x_min, f_min = midpoint_method(a, b, epsilon)
print(f"Минимальное значение f(x) в методе средней точки примерно равно {f_min} при x = {x_min}")
