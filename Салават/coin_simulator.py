import random


def flip_coin(n):
    heads_count = 0
    for i in range(n):
        toss = random.randint(0, 1)
        if toss == 1:
            heads_count += 1
    return heads_count


import time


def run_single_experiment(n):
    start_time = time.perf_counter()

    # 1. Вызываем функцию flip_coin(n) и сохраняем результат
    heads = flip_coin(n)

    end_time = time.perf_counter()

    # 2. Вычисляем время работы
    elapsed_time = end_time - start_time

    # 3. Вычисляем частоту выпадения орла
    frequency = heads / n

    # 4. Вычисляем отклонение от 0.5
    deviation = abs(frequency - 0.5)

    # Возвращаем все три значения
    return frequency, deviation, elapsed_time


def run_series(n, num_runs=5):
    frequencies = []
    deviations = []
    times = []

    for i in range(num_runs):
        frequency, deviation, elapsed_time = run_single_experiment(n)
        frequencies.append(frequency)
        deviations.append(deviation)
        times.append(elapsed_time)

    avg_fr = sum(frequencies) / len(frequencies)
    avg_dev = sum(deviations) / len(deviations)
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    return frequencies, avg_fr, avg_dev, avg_time, min_time, max_time


print(run_series(10))


import matplotlib.pyplot as plt

# --- 1. Готовим данные для графиков ---
# По оси X у нас количество бросков монеты (N)
n_values = [10, 100, 1000, 10000, 100000, 1000000, 3000000, 5000000, 10000000]

# По оси Y для первого графика — средние отклонения
# ВНИМАНИЕ: Замените эти цифры на результаты ваших собственных измерений из таблицы!
deviations = [0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352,
0.00000453999645203352
]

# По оси Y для второго графика — среднее время работы в секундах
# ВНИМАНИЕ: Замените эти цифры на ваши замеры времени!
times = [0.000002500019036233425,
0.000002500001573935151,
0.00023114000214263797,
0.0002337199985049665,
0.004630819999147206,
0.029513779981061816,
0.1939368800027296,
1.4415532999904825,
 2.7857533599832096
]

# --- 2. Строим первый график (Точность симуляции) ---
plt.figure(figsize=(6, 4))  # Создаем окно для графика размером 6 на 4 дюйма

# Рисуем линию графика:
plt.plot(n_values, deviations, marker='o', color='green', linewidth=2)
# marker='o' — ставит круглые точки в местах наших замеров
# color='green' — красит линию в зеленый цвет
# linewidth=2 — делает линию более жирной и заметной

# Настраиваем оси:
plt.xscale('log')  # Включаем логарифмический масштаб для оси X,
# чтобы точки 10, 100, 1000 и 1000000 стояли на равном расстоянии друг от друга

# Подписываем график и оси:
plt.title('Точность симуляции (Закон больших чисел)')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Среднее отклонение от 0.5')
plt.grid(True)  # Включаем сеточку на заднем фоне, чтобы было легче смотреть значения

plt.tight_layout()  # Делаем так, чтобы все подписи влезли в картинку
plt.savefig('chart_deviation.png')  # Сохраняем график на компьютер как картинку
plt.show()  # Показываем график на экране

# --- 3. Строим второй график (Производительность программы) ---
plt.figure(figsize=(6, 4))  # Создаем новое окно для второго графика

# Рисуем линию графика времени:
plt.plot(n_values, times, marker='s', color='red', linewidth=2)
# marker='s' — ставит квадратные точки (square)
# color='red' — красит линию в красный цвет

# Подписываем график и оси:
plt.title('Время работы программы')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Время выполнения (в секундах)')
plt.grid(True)  # Тоже включаем сетку

plt.tight_layout()
plt.savefig('chart_time.png')  # Сохраняем второй график как картинку
plt.show()  # Показываем на экране
