import random

import plt


def flip_coin(n):
    heads_count = 0
    for i in range(n):
        brosok = random.randint(0, 1)
        if brosok == 1:
            heads_count += 1
    return heads_count


import time


def run_single_experiment(n):
    start_time = time.perf_counter()
    heads = flip_coin(n)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    frequency = heads / n

    deviation = abs(frequency - 0.5)

    return frequency, deviation, elapsed_time


def run_series(n, num_runs=5):
    freq = []
    dev = []
    et = []
    for i in range(num_runs):
        frequency, deviation, elapsed_time = run_single_experiment(n)
        freq.append(frequency)
        dev.append(deviation)
        et.append(elapsed_time)

    avg_freq = sum(freq) / len(freq)
    avg_dev = sum(dev) / len(dev)
    avg_et = sum(et) / len(et)
    max_et = max(et)
    min_et = min(et)

    return freq, avg_freq, avg_dev, avg_et, min_et, max_et


n = [10, 100, 1000, 10_000, 100_000, 1_000_000]

for i in n:
    print(run_series(i))

    # --- 1. Готовим данные для графиков ---
    # По оси X у нас количество бросков монеты (N)
    n_values = [10, 100, 1000, 10000, 100000, 1000000]

    # По оси Y для первого графика — средние отклонения
    # ВНИМАНИЕ: Замените эти цифры на результаты ваших собственных измерений из таблицы!
    deviations = [0.06, 0.04200000000000002, 0.0064000000000000055, 0.002100000000000002, 0.0007039999999999824, 0.0005833999999999895]

    # По оси Y для второго графика — среднее время работы в секундах
    # ВНИМАНИЕ: Замените эти цифры на ваши замеры времени!
    times = [0.000007560010999441147, 0.000000064000000000000055, 0.0004869399592280388, 0.004847719939425588, 0.06144440001808107, 0.563755919970572]

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
