def print_result(func):
    def wrapper(*args, **kwargs):
        # Вызываем исходную функцию
        result = func(*args, **kwargs)
        
        # Выводим имя функции
        print(func.__name__)
        
        # Обрабатываем результат в зависимости от типа
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        
        # Возвращаем результат исходной функции
        return result
    return wrapper


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()