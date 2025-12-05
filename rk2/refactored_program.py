class ProgrammingLanguage:
    """Класс 'Язык программирования'"""
    def __init__(self, id, name, popularity_score, ide_id):
        self.id = id
        self.name = name
        self.popularity_score = popularity_score  
        self.ide_id = ide_id  

    def __repr__(self):
        return f"ProgrammingLanguage(id={self.id}, name='{self.name}', popularity={self.popularity_score}, ide_id={self.ide_id})"


class IDE:
    """Класс 'Средство разработки' (Integrated Development Environment)"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"IDE(id={self.id}, name='{self.name}')"


class LanguageIDE:
    """Класс для связи многие-ко-многим между Языком программирования и Средством разработки"""
    def __init__(self, language_id, ide_id):
        self.language_id = language_id
        self.ide_id = ide_id

    def __repr__(self):
        return f"LanguageIDE(language_id={self.language_id}, ide_id={self.ide_id})"


class ProgrammingSystem:
    """Основной класс для работы с данными"""
    def __init__(self, ides, languages, language_ide_links):
        self.ides = ides
        self.languages = languages
        self.language_ide_links = language_ide_links
    
    def get_test_data(self):
        """Возвращает тестовые данные"""
        return {
            'ides': self.ides,
            'languages': self.languages,
            'language_ide_links': self.language_ide_links
        }
    
    def task1(self):
        """Задание 1: Список всех средств разработки, у которых в названии присутствует слово 'Studio' или 'VS', 
        и список языков программирования, которые с ними связаны"""
        result = {}
        
        # Находим IDE с нужными названиями
        target_ides = [ide for ide in self.ides if 'Studio' in ide.name or 'VS' in ide.name]
        
        for ide in target_ides:
            # Находим языки, связанные с этим IDE (один-ко-многим)
            related_languages = [lang for lang in self.languages if lang.ide_id == ide.id]
            result[ide.name] = [lang.name for lang in related_languages]
        
        return result
    
    def task2(self):
        """Задание 2: Список средств разработки со средней популярностью языков в каждом IDE, 
        отсортированный по средней популярности"""
        result = []
        
        # Группируем языки по IDE
        ide_languages = {}
        for lang in self.languages:
            if lang.ide_id not in ide_languages:
                ide_languages[lang.ide_id] = []
            ide_languages[lang.ide_id].append(lang)
        
        # Вычисляем среднюю популярность для каждого IDE
        for ide_id, lang_list in ide_languages.items():
            ide_name = next(ide.name for ide in self.ides if ide.id == ide_id)
            total_popularity = sum(lang.popularity_score for lang in lang_list)
            avg_popularity = total_popularity / len(lang_list)
            result.append((ide_name, round(avg_popularity, 2)))
        
        # Сортируем по средней популярности
        result.sort(key=lambda x: x[1])
        
        return result
    
    def task3(self):
        """Задание 3: Список всех языков программирования, у которых название начинается с буквы 'C', 
        и названия средств разработки, которые с ними связаны"""
        result = {}
        
        # Находим языки, начинающиеся на 'C'
        c_languages = [lang for lang in self.languages if lang.name.startswith('C')]
        
        for lang in c_languages:
            # Находим IDE, связанные с этим языком (многие-ко-многим)
            related_ide_ids = [link.ide_id for link in self.language_ide_links if link.language_id == lang.id]
            related_ides = [ide for ide in self.ides if ide.id in related_ide_ids]
            
            result[lang.name] = [ide.name for ide in related_ides]
        
        return result


def create_test_data():
    """Создание тестовых данных"""
    # Список средств разработки
    ides = [
        IDE(1, "Visual Studio"),
        IDE(2, "IntelliJ IDEA"),
        IDE(3, "PyCharm"),
        IDE(4, "Eclipse"),
        IDE(5, "VS Code")
    ]
    
    # Список языков программирования (связь один-ко-многим с IDE)
    languages = [
        ProgrammingLanguage(1, "Python", 95, 3),
        ProgrammingLanguage(2, "Java", 88, 2),
        ProgrammingLanguage(3, "C#", 85, 1),
        ProgrammingLanguage(4, "JavaScript", 92, 5),
        ProgrammingLanguage(5, "C++", 78, 1)
    ]
    
    # Список для связи многие-ко-многим
    language_ide_links = [
        LanguageIDE(1, 3),  # Python поддерживается в PyCharm
        LanguageIDE(1, 5),  # Python - VS Code
        LanguageIDE(2, 2),  # Java - IntelliJ IDEA
        LanguageIDE(2, 4),  # Java - Eclipse
        LanguageIDE(3, 1),  # C# - Visual Studio
        LanguageIDE(4, 5),  # JavaScript - VS Code
        LanguageIDE(5, 1),  # C++ - Visual Studio
        LanguageIDE(5, 5),  # C++ - VS Code
    ]
    
    return ides, languages, language_ide_links


def main():
    """Основная функция программы"""
    print("РУБЕЖНЫЙ КОНТРОЛЬ - ВАРИАНТ 12")
    print("Классы: Язык программирования - Средство разработки\n")
    
    # Создаем данные и систему
    ides, languages, links = create_test_data()
    system = ProgrammingSystem(ides, languages, links)
    
    # Вывод тестовых данных
    print("ТЕСТОВЫЕ ДАННЫЕ:")
    print("Средства разработки:", ides)
    print("Языки программирования:", languages)
    print("Связи многие-ко-многим:", links)
    print("\n" + "="*50 + "\n")
    
    # Выполнение заданий
    print("=== ЗАДАНИЕ 1 ===")
    print("Средства разработки, содержащие 'Studio' или 'VS', и связанные языки программирования:")
    task1_result = system.task1()
    for ide_name, langs in task1_result.items():
        print(f"\n{ide_name}:")
        for lang in langs:
            print(f"  - {lang}")
    
    print("\n=== ЗАДАНИЕ 2 ===")
    print("Средства разработки со средней популярностью языков (отсортировано):")
    task2_result = system.task2()
    for ide_name, avg_pop in task2_result:
        print(f"{ide_name}: {avg_pop}")
    
    print("\n=== ЗАДАНИЕ 3 ===")
    print("Языки программирования, начинающиеся на 'C', и связанные средства разработки:")
    task3_result = system.task3()
    for lang_name, ides_list in task3_result.items():
        print(f"\n{lang_name}:")
        for ide_name in ides_list:
            print(f"  - {ide_name}")


if __name__ == "__main__":
    main()