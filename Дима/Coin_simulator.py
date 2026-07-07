import random
import time
import matplotlib.pyplot as plt

# --- 1. Готовим данные для графиков ---
# По оси X у нас количество бросков монеты (N)
n_values = [10, 100, 1000, 10000, 100000, 1000000]

# По оси Y для первого графика — средние отклонения
# ВНИМАНИЕ: Замените эти цифры на результаты ваших собственных измерений из таблицы!
deviations = [0.1599999999, 0.0619999999, 0.0072, 0.0048, 0.0011, 0.0004696]

# По оси Y для второго графика — среднее время работы в секундах
# ВНИМАНИЕ: Замените эти цифры на ваши замеры времени!
times = [0.0000347999, 0.0001495800, 0.00101476, 0.01131896, 0.09194654, 0.9456832399]


def flip_coin(n):
    count_eagle = 0
    count_reshka = 0
    for i in range(n+1):
        brosok = random.randint(0, 1)       # Имитируем один бросок монеты
        if brosok == 1:
            count_eagle += 1
        else:
            count_reshka += 1
    return count_eagle

def run_single_experiment(n):
    start_time = time.perf_counter()
    eagles = flip_coin(n)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    frequency = eagles / n
    deviation = abs(frequency - 0.5)
    return frequency, deviation, elapsed_time
# print(run_single_experiment(10))

def run_series(n, num_runs=5):
    frequency = []
    deviation = []
    elapsed_time = []
    for i in range(num_runs):
        fr, dev, et = run_single_experiment(n)
        frequency.append(fr)
        deviation.append(dev)
        elapsed_time.append(et)
    average_freq = sum(frequency) / len(frequency)
    average_dev = sum(deviation) / len(deviation)
    average_et = sum(elapsed_time) / len(elapsed_time)
   
    max_et = max(elapsed_time)
    min_et = min(elapsed_time)

    return frequency, average_freq, average_dev, average_et, min_et, max_et

# --- 2. Строим первый график (Точность симуляции) ---
plt.figure(figsize=(6, 4)) # Создаем окно для графика размером 6 на 4 дюйма

# Рисуем линию графика:
plt.plot(n_values, deviations, marker='o', color='green', linewidth=2)
# marker='o' — ставит круглые точки в местах наших замеров
# color='green' — красит линию в зеленый цвет
# linewidth=2 — делает линию более жирной и заметной

# Настраиваем оси:
plt.xscale('log') # Включаем логарифмический масштаб для оси X,
                  # чтобы точки 10, 100, 1000 и 1000000 стояли на равном расстоянии друг от друга

# Подписываем график и оси:
plt.title('Точность симуляции (Закон больших чисел)')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Среднее отклонение от 0.5')
plt.grid(True) # Включаем сеточку на заднем фоне, чтобы было легче смотреть значения

plt.tight_layout() # Делаем так, чтобы все подписи влезли в картинку
plt.savefig('chart_deviation.png') # Сохраняем график на компьютер как картинку
plt.show() # Показываем график на экране


# --- 3. Строим второй график (Производительность программы) ---
plt.figure(figsize=(6, 4)) # Создаем новое окно для второго графика

# Рисуем линию графика времени:
plt.plot(n_values, times, marker='s', color='red', linewidth=2)
# marker='s' — ставит квадратные точки (square)
# color='red' — красит линию в красный цвет

# Подписываем график и оси:
plt.title('Время работы программы')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Время выполнения (в секундах)')
plt.grid(True) # Тоже включаем сетку

plt.tight_layout()
plt.savefig('chart_time.png') # Сохраняем второй график как картинку
plt.show() # Показываем на экране

