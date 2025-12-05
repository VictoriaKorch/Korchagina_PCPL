class Unique(object):
    def __init__(self, items, **kwargs):
        # Получаем значение ignore_case из kwargs, по умолчанию False
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()
        self.iterator = self._generate_unique()
    
    def _generate_unique(self):
        for item in self.items:
            # Определяем ключ для сравнения
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item
            
            # Если элемента еще не было, добавляем его в множество и возвращаем
            if key not in self.seen:
                self.seen.add(key)
                yield item
    
    def __next__(self):
        return next(self.iterator)
    
    def __iter__(self):
        return self


if __name__ == "__main__":
    print("Тест 1: числовые данные с дубликатами")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
    print(f"Исходные данные: {data1}")
    print("Результат Unique(data1):", end=" ")
    for item in Unique(data1):
        print(item, end=" ")
    print()
    
    print("\nТест 2: строковые данные без ignore_case")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"Исходные данные: {data2}")
    print("Результат Unique(data2):", end=" ")
    for item in Unique(data2):
        print(item, end=" ")
    print()
    
    print("\nТест 3: строковые данные с ignore_case=True")
    print(f"Исходные данные: {data2}")
    print("Результат Unique(data2, ignore_case=True):", end=" ")
    for item in Unique(data2, ignore_case=True):
        print(item, end=" ")
    print()
    
    print("\nТест 4: работа с генератором")
    from gen_random import gen_random
    data3 = gen_random(10, 1, 3)
    print("gen_random(10, 1, 3) -> Unique(data3):", end=" ")
    for item in Unique(data3):
        print(item, end=" ")
    print()
    
    print("\nТест 5: смешанные строки с разным регистром")
    data4 = ['Hello', 'hello', 'WORLD', 'world', 'Hello', 'HELLO']
    print(f"Исходные данные: {data4}")
    print("Unique(data4):", end=" ")
    for item in Unique(data4):
        print(item, end=" ")
    print()
    
    print("Unique(data4, ignore_case=True):", end=" ")
    for item in Unique(data4, ignore_case=True):
        print(item, end=" ")
    print()