def f(x):
    return x ** 3 + 2 * x ** 2 + x
def df(x):
    return 3 * x ** 2 + 4 * x + 1
def ddf(x):
    return 6 * x + 4
def newton_method(x0, epsilon=1e-6, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        # Вычисляем значения первой и второй производных в точке x
        fx_prime = df(x)
        fx_double_prime = ddf(x)

        if fx_double_prime == 0:  # Проверка на случай, если вторая производная равна нулю
            print("Вторая производная равна нулю. Метод Ньютона не применим.")
            return None, None

        x_new = x - fx_prime / fx_double_prime  # Шаг метода Ньютона

        if abs(x_new - x) < epsilon:  # Проверка на достижение необходимой точности
            x_min = x_new
            f_min = f(x_min)
            return x_min, f_min

        x = x_new  # Обновляем x для следующей итерации

    print("Достигнуто максимальное количество итераций. Минимум не найден.")
    return None, None

x0 = -0.5  # Начальная точка
epsilon = 1e-6

x_min, f_min = newton_method(x0, epsilon)
if x_min is not None:
    print(f"Минимальное значение f(x) примерно равно {f_min} при x = {x_min}")
else:
    print("Минимум не найден.")
