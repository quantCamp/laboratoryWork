import random
import time

import plt


def flip_coin(n):
    heads_count = 0

    for _ in range(n):
        toss = random.randint(0, 1)
        if toss == 1:
            heads_count += 1

    return heads_count


def run_single_experiment(n):
    start_time = time.perf_counter() # Начало выполнения функции heads = flip_coin(n)

    heads = flip_coin(n)

    end_time = time.perf_counter() # Конец выполнения функции heads = flip_coin(n)

    elapsed_time = end_time - start_time

    frequency = heads / n # Находим частоту выпадения орла

    deviation = abs(frequency - 0.5)

    return frequency, deviation, elapsed_time # Возвращаем полученные значения


def run_series(n, num_runs=5):
    # Объявление списков
    frequency_list = []
    time_work_list = []
    deviation_list = []

    for _ in range(num_runs):
        frequency, deviation, elapsed_time = run_single_experiment(n)

        frequency_list.append(frequency)
        time_work_list.append(elapsed_time)
        deviation_list.append(deviation)

        # Вычисляем среднее значение списков
    frequency_value = sum(frequency_list) / len(frequency_list)
    time_work_value = sum(time_work_list) / len(time_work_list)
    deviation_value = sum(deviation_list) / len(deviation_list)

    max_time = max(time_work_list)
    min_time = min(time_work_list)

    return frequency_list, frequency_value, time_work_value, deviation_value, max_time, min_time # Возвращаем значения



# --- 1. Готовим данные для графиков ---
# По оси X у нас количество бросков монеты (N)
n_values = [10, 100, 1000, 10000, 100000, 1000000, 3000000, 5000000]


# По оси Y для первого графика — средние отклонения
# ВНИМАНИЕ: Замените эти цифры на результаты ваших собственных измерений из таблицы!
deviations = []

# По оси Y для второго графика — среднее время работы в секундах
# ВНИМАНИЕ: Замените эти цифры на ваши замеры времени!
times = []

for n in n_values:
    freq_list, frequency_value, time_work_value, deviation_value, max_time, min_time = run_series(n)
    deviations.append(deviation_value)
    times.append(time_work_value)
    print(n, freq_list, frequency_value, time_work_value, deviation_value, max_time, min_time)
    print(f"""
    Проводим серию для N = {n} бросков...
    Запуски(частота орла): {freq_list}
    Средняя частота: {frequency_value} | Среднее отклонение: {time_work_value}
    Время выполнения: среднее = {deviation_value} сек | макс = {max_time} сек | мин = {min_time}сек
    """)


plt.figure(figsize=(6, 4))
plt.plot(n_values, deviations, marker='o', color='green', linewidth=2)
plt.xscale('log')
plt.title('Точность симуляции (Закон больших чисел)')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Среднее отклонение от 0.5')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart_deviation.png')
plt.show()
plt.figure(figsize=(6, 4))


plt.plot(n_values, times, marker='s', color='red', linewidth=2)


plt.title('Время работы программы')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Время выполнения (в секундах)')
plt.grid(True)

plt.tight_layout()
plt.savefig('chart_time.png')
plt.show()