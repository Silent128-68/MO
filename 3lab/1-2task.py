def f(x):
    return x ** 3 + 2 * x ** 2 + x
def df(x):
    return 3 * x ** 2 + 4 * x + 1
def chord_method(a, b, epsilon=1e-6):
    while (b - a) / 2 > epsilon:
        x_hord = a - df(a) * (a - b) / (df(a) - df(b))  # Шаг 1: Находим точку пересечения x̄ по формуле
        df_hord = df(x_hord)

        if abs(df_hord) <= epsilon:  # Шаг 2: Проверка на окончание поиска
            # Если производная близка к нулю, считаем, что найден минимум
            x_min = x_hord
            f_min = f(x_hord)
            return x_min, f_min

        if df_hord > 0:  # Шаг 3: Переход к новому отрезку
            b = x_hord  # Если производная положительна, сдвигаем верхнюю границу
        else:
            a = x_hord  # Если производная отрицательна, сдвигаем нижнюю границу

a = -0.9
b = 0.5
epsilon = 1e-6

x_min, f_min = chord_method(a, b, epsilon)
print(f"Минимальное значение f(x) в методе хорд примерно равно {f_min} при x = {x_min}")
