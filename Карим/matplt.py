import matplotlib.pyplot as plt


n_values = [10, 100, 1000, 10000, 100000, 1000000]
deviations = [0.07999999999999999, 0.05400000000000001, 0.013400000000000013, 0.0025599999999999954, 0.0015759999999999884, 0.00036620000000000543]
times = [0.000014140200028123217, 0.000052111199966020647, 0.0005201136000096085, 0.005559599599996546, 0.0525527172000011, 0.5093700509999962]

# --- Первый график (Точность симуляции) ---
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

# --- Второй график (Производительность программы) ---
plt.figure(figsize=(6, 4))
plt.plot(n_values, times, marker='s', color='red', linewidth=2)

plt.title('Время работы программы')
plt.xlabel('Количество бросков (N)')
plt.ylabel('Время выполнения (в секундах)')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart_time.png')
plt.show()