import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    # Тест из задания
    print("Тест: gen_random(5, 1, 3)")
    print("Ожидается: 5 случайных чисел в диапазоне от 1 до 3, например: 2, 2, 3, 2, 1")
    print("Результат:")
    result = list(gen_random(5, 1, 3))
    print(", ".join(map(str, result)))
    
    # Дополнительные тесты
    print("\nДополнительные тесты:")
    
    print("gen_random(3, 10, 15):")
    result2 = list(gen_random(3, 10, 15))
    print(", ".join(map(str, result2)))
    
    print("gen_random(1, -5, 5):")
    result3 = list(gen_random(1, -5, 5))
    print(", ".join(map(str, result3)))
    
    print("gen_random(0, 1, 10) (0 чисел):")
    result4 = list(gen_random(0, 1, 10))
    print(f"Результат: {result4} (пустой список)")