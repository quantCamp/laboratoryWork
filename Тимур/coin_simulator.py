#Задание 1
import random
import time





def flip_coin(n):
    heads_count = 0
    for _ in range(n):
        heads_count += random.randint(0, 1)
    return heads_count

def run_single_experiment(n):
    start_time = time.perf_counter()

    heads = flip_coin(n)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    frequency = heads / n
    deviation = abs(frequency - 0.5)

    return frequency, deviation, elapsed_time

def run_series(n, num_runs=5):
    elapsed_time_list = []
    frequency_list = []
    deviation_list = []
    for _ in range(num_runs):
        run_single_result = run_single_experiment(n)
        elapsed_time_list += [run_single_result[2]]
        frequency_list += [run_single_result[0]]
        deviation_list += [run_single_result[1]]

    print(f"Запуски (частота орла): {frequency_list}")
    max_elapsed_time = max(elapsed_time_list)
    min_elapsed_time = min(elapsed_time_list)
    average_value_elapsed_time = sum(elapsed_time_list) / len(elapsed_time_list)
    average_value_frequency = sum(frequency_list) / len(frequency_list)
    average_value_deviation = sum(deviation_list) / len(deviation_list)
    return average_value_frequency, average_value_deviation, average_value_elapsed_time, min_elapsed_time ,max_elapsed_time

result = run_series(int(input("Введите количество бросков ")))
print(f"Средняя частота: {result[0]} | Среднее отклонение: {result[1]}")
print(f"Время выполнения: среднее = {result[2]} сек | мин = {result[3]} сек | макс = {result[4]} сек")
