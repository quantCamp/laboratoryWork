#Задание 1
import random

def flip_coin(n):
    heads_count = 0

    for _ in range(n):
        coin = random.randint(0, 1)
        if coin == 1:
            heads_count += 1

    return heads_count



#Задание 2

import time


def run_single_experiment(n):
    start_time = time.perf_counter()

    heads = flip_coin(n)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    frequency = heads / n

    deviation = abs(frequency - 0.5)

    return frequency, deviation, elapsed_time

#Задание 3

def run_series(n, num_runs=5):
    frequencies = []
    deviations = []
    times = []

    for _ in range(num_runs):
        freq, dev, exec_time = run_single_experiment(n)

        frequencies.append(freq)
        deviations.append(dev)
        times.append(exec_time)

    avg_freq = sum(frequencies) / len(frequencies)
    avg_dev = sum(deviations) / len(deviations)
    avg_time = sum(times) / len(times)

    min_time = min(times)
    max_time = max(times)

    print(f"=== Результаты серии из {num_runs} экспериментов (n={n}) ===")
    print(f"• Средняя частота орлов:        {avg_freq:.4f}")
    print(f"• Среднее отклонение от 0.5:    {avg_dev:.4f}")
    print(f"• Среднее время работы:         {avg_time:.6f} сек.")
    print(f"• Минимальное время работы:     {min_time:.6f} сек.")
    print(f"• Максимальное время работы:    {max_time:.6f} сек.")
    print("=" * 50)

    return avg_freq, avg_dev, avg_time

#Экспериментальная часть

print("ЗАПУСК ЭКСПЕРИМЕНТАЛЬНОЙ ЧАСТИ\n")
steps = [10, 100, 1000, 10000, 100000, 1000000, 3000000, 5000000]
for step in steps:
    run_series(step)

#Построение графика

import matplotlib.pyplot as plt

n_values = [10, 100, 1000, 10000, 100000, 1000000]

deviations = [0.1400, 0.0140, 0.0086, 0.0016, 0.0001, 0.0002]

times = [0.000023, 0.000100, 0.001013, 0.010052, 0.100216, 0.989523]


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