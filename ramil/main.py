import random

import time


def run_single_experiment(n):
    start_time = time.perf_counter()
    heads = flip_coin(n)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    frequency = heads / n
    deviation = abs(frequency - 0.5)
    return frequency, deviation, elapsed_time


def flip_coin(n):
    heads_count = 0
    for i in range(n):
        heads_count += random.randint(0, 1)
    return heads_count


def run_series(n, num_runs=5):
    frequencies = []
    deviations = []
    elapsed_times = []
    max_time = 0
    min_time = 1000
    print(f"Запуск проверки для {n} бросков")
    print(" Частоты выпадения орлов: ", end="")
    for i in range(num_runs):
        frequency, deviation, elapsed_time = run_single_experiment(n)
        frequencies.append(frequency)
        deviations.append(deviation)
        elapsed_times.append(elapsed_time)
        max_time = max(max_time, elapsed_time)
        min_time = min(min_time, elapsed_time)
        print(frequency, end=", ")
    middle_frequencies = sum(frequencies) / len(frequencies)
    middle_deviations = sum(deviations) / len(deviations)
    middle_elapsed_times = sum(elapsed_times) / len(elapsed_times)
    print(f"""  Средняя частота: {middle_frequencies} | Среднее отклонение: {middle_deviations}
  Время выполнения: среднее = {middle_elapsed_times} сек | мин = {min_time} сек | макс = {max_time} сек""")
    print()


for i in range(1, 6):
    run_series(10 ** i)

print("Эксперимент завершён!")
