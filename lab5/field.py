def field(items, *args):
    """
    Генератор для извлечения значений из словарей.
    
    Args:
        items: Список словарей
        *args: Ключи для извлечения (один или несколько)
    
    Yields:
        Если один аргумент - значения ключа
        Если несколько аргументов - словари с указанными ключами
    """
    if len(args) == 0:
        raise ValueError("At least one field must be specified")
    
    # Если передан один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            if _has_valid_field(item, key):
                yield item[key]
    # Если передано несколько аргументов
    else:
        for item in items:
            result = {}
            has_valid_fields = False
            
            for key in args:
                if _has_valid_field(item, key):
                    result[key] = item[key]
                    has_valid_fields = True
            
            # Если есть хотя бы одно поле с не-None значением
            if has_valid_fields:
                yield result

def _has_valid_field(item, key):
    """Вспомогательная функция для проверки валидности поля"""
    return key in item and item[key] is not None


if __name__ == "__main__":
    # Тестовые данные из задания
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    
    print("Тест 1: field(goods, 'title')")
    print("Ожидается: 'Ковер', 'Диван для отдыха'")
    print("Результат:")
    for item in field(goods, 'title'):
        print(f"  {item}")
    
    print("\nТест 2: field(goods, 'title', 'price')")
    print("Ожидается: {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}")
    print("Результат:")
    for item in field(goods, 'title', 'price'):
        print(f"  {item}")