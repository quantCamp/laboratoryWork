import random
import time

def flip_coin(n) -> int:
    heads_count = 0
    for i in range(n):
        randint_result = random.randint(0, 1)
        if randint_result == 1:
            heads_count += 1
    return heads_count

def single_experiment(n) -> tuple:
    start_time = time.perf_counter()
    heads = flip_coin(n)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    heads_frequency = heads / n
    deviation = abs(heads_frequency - 0.5)
    return heads_frequency, deviation, elapsed_time

def run_series(n_runs=5) -> None:
    flip_nums = [10, 100, 1000, 10000, 100000, 1000000]
    average_deviations = []
    average_elapsed_times = []
    average_head_frequencies = []
    max_time = []
    min_time = []
    for i in flip_nums:
        head_frequency = []
        deviations = []
        elapsed_time = []
        for n in range(n_runs):
            experiment = single_experiment(i)
            print(f"номер {n} эксперимент для {i} бросков: частота орлов {experiment[0]}; отклонение от 0.5 {experiment[1]}; затраченное время {experiment[2]}")
            head_frequency.append(experiment[0])
            deviations.append(experiment[1])
            elapsed_time.append(experiment[2])
        average_deviations.append(sum(deviations) / len(deviations))
        average_elapsed_times.append(sum(elapsed_time) / len(elapsed_time))
        average_head_frequencies.append(sum(head_frequency) / len(head_frequency))
        max_time.append(max(elapsed_time))
        min_time.append(min(elapsed_time))
        print("--------------------------------")
    print("\nСредние показатели для всех бросков:\n")
    for index, i in enumerate(flip_nums):
        print(f"Среднее отклонение для {i} бросков: {average_deviations[index]}")
        print(f"Среднее затраченное время для {i} бросков: {average_elapsed_times[index]}")
        print(f"Минимальное затраченное время для {i} бросков: {min_time[index]}")
        print(f"Максимальное затраченное время для {i} бросков: {max_time[index]}")
        print(f"Средняя частота орлов для {i} бросков: {average_head_frequencies[index]}")
        print("--------------------------------")

run_series()