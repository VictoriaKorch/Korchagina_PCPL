import json
import sys
import os
from random import randint
from print_result import print_result
from cm_timer import cm_timer_1

# Получаем путь к файлу из аргументов командной строки или используем путь по умолчанию
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    # Укажите путь к вашему файлу данных по умолчанию
    path = 'data_light.json'  # или другой путь к вашему файлу
    # Либо можно использовать относительный путь:
    # path = os.path.join('lab_python_fp', 'data.json')

# Проверяем существование файла перед открытием
if not os.path.exists(path):
    print(f"Ошибка: файл '{path}' не найден")
    print("Укажите путь к файлу как аргумент командной строки:")
    print("python process_data.py <путь_к_файлу>")
    sys.exit(1)

try:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Ошибка: файл '{path}' не найден")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Ошибка при чтении JSON: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
    sys.exit(1)

@print_result
def f1(arg):
    return sorted({result_1['job-name'].lower() for result_1 in arg if 'job-name' in result_1}, key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [randint(100000, 200000) for i in arg]
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))