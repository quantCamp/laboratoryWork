# Задание 1
import random, time
import matplotlib.pyplot as plt


n_values = [10, 100, 1000, 10000, 100000, 1000000]
for n in n_values:
    def flip_coin(n):
        heads_count = 0
        for i in range(n):
            chance = random.randint(0, 1)
            if chance == 1:
                heads_count += 1
        return heads_count


    # Задание 2

    def run_single_experiment(n):
        start_time = time.perf_counter()
        
        heads = flip_coin(n)
        
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        
        frequency = heads / n
        
        deviation = abs(frequency - 0.5)
        
        return frequency, deviation, elapsed_time
        




    # Задание 3

    count_heads = []
    otclonenie = []
    time_list = []

    def run_series(n, num_runs = 5):
        for i in range(num_runs):
            frequency, deviation, elapsed_time = run_single_experiment(n)
            print(frequency)
            count_heads.append(frequency)
            otclonenie.append(deviation)
            time_list.append(elapsed_time)
        average_value_heads = sum(count_heads) / len(count_heads)
        average_value_otclonenie = sum(otclonenie) / len(otclonenie)
        average_value_time = sum(time_list) / len(time_list)
        max_time = max(time_list)
        min_time = min(time_list)
        return average_value_heads , average_value_otclonenie, average_value_time, max_time, min_time


# --- 1. Готовим данные для графиков ---
# По оси X у нас количество бросков монеты (N)
n_values = [10, 100, 1000, 10000, 100000, 1000000]

# По оси Y для первого графика — средние отклонения
# ВНИМАНИЕ: Замените эти цифры на результаты ваших собственных измерений из таблицы!
deviations = [0.16, 0.02400000000000001, 0.01020000000000001, 0.0038999999999999924, 0.0009939999999999838, 0.00022479999999999167]

# По оси Y для второго графика — среднее время работы в секундах
# ВНИМАНИЕ: Замените эти цифры на ваши замеры времени!
times = [0.000002480000077630393, 0.000057999999808089345, 0.00043931999971391633, 0.005635720000100264, 0.04627734000005148, 0.4589369400000578]


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

