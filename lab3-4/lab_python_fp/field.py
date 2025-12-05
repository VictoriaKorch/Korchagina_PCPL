def field(items, *args):
    assert len(args) > 0
    
    # Если передан один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    # Если передано несколько аргументов
    else:
        for item in items:
            result = {}
            has_valid_fields = False
            
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True
            
            # Если есть хотя бы одно поле с не-None значением
            if has_valid_fields:
                yield result


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
    
    # Дополнительные тесты с None значениями
    print("\nТест 3: с None значениями")
    goods_with_none = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},  # нет price
        {'title': None, 'price': 1500},  # title = None
        {'price': 3000}  # нет title
    ]
    
    print("field(goods_with_none, 'title'):")
    for item in field(goods_with_none, 'title'):
        print(f"  {item}")
    
    print("\nfield(goods_with_none, 'title', 'price'):")
    for item in field(goods_with_none, 'title', 'price'):
        print(f"  {item}")