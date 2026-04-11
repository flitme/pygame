# Класс тайла

import time

# Переменная для хранения точки отсчета
start_point = None

def start_timer():
    global start_point
    start_point = time.perf_counter()
    print("Таймер запущен!")

def get_current_time():
    if start_point is None:
        return "Таймер еще не запущен"
    return time.perf_counter() - start_point

# Пример использования:
start_timer()

# Имитируем какую-то работу
time.sleep(2.5)

print(start_point)
print(f"Прошло времени: {get_current_time():.2f} сек.")