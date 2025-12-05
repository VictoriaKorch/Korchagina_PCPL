import unittest
from refactored_program import ProgrammingSystem, create_test_data, IDE, ProgrammingLanguage, LanguageIDE


class TestProgrammingSystem(unittest.TestCase):
    """Тесты для системы программирования"""
    
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        ides, languages, links = create_test_data()
        self.system = ProgrammingSystem(ides, languages, links)
    
    def test_task1_studio_vs_ides_and_languages(self):
        """Тест задания 1: проверка IDE с 'Studio' или 'VS' и связанных языков"""
        result = self.system.task1()
        
        print("\n[Тест 1] Проверка IDE с 'Studio' или 'VS' и связанных языков")
        print(f"Найдено IDE: {list(result.keys())}")
        
        # Проверяем, что найдены правильные IDE
        expected_ides = {"Visual Studio", "VS Code"}
        self.assertEqual(set(result.keys()), expected_ides)
        
        # Проверяем языки для Visual Studio
        self.assertEqual(sorted(result["Visual Studio"]), ["C#", "C++"])
        print("  ✓ Visual Studio содержит C# и C++")
        
        # Проверяем языки для VS Code
        self.assertEqual(sorted(result["VS Code"]), ["JavaScript"])
        print("  ✓ VS Code содержит JavaScript")
    
    def test_task2_average_popularity_sorted(self):
        """Тест задания 2: проверка средней популярности и сортировки"""
        result = self.system.task2()
        
        print("\n[Тест 2] Проверка средней популярности языков по IDE")
        print(f"Результат: {result}")
        
        # Проверяем структуру результата
        # Должно быть 4 записи (Eclipse не имеет связанных языков в связи один-ко-многим)
        self.assertEqual(len(result), 4)
        print(f"  ✓ Найдено {len(result)} IDE с языками")
        
        # Проверяем, что результат отсортирован по возрастанию средней популярности
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i][1], result[i + 1][1])
        print("  ✓ Результат корректно отсортирован")
        
        # Проверяем конкретные значения
        result_dict = dict(result)
        self.assertEqual(result_dict["Visual Studio"], 81.5)  # (85 + 78) / 2
        print("  ✓ Visual Studio: средняя популярность 81.5")
        
        self.assertEqual(result_dict["IntelliJ IDEA"], 88.0)
        print("  ✓ IntelliJ IDEA: средняя популярность 88.0")
        
        self.assertEqual(result_dict["VS Code"], 92.0)
        print("  ✓ VS Code: средняя популярность 92.0")
        
        self.assertEqual(result_dict["PyCharm"], 95.0)
        print("  ✓ PyCharm: средняя популярность 95.0")
    
    def test_task3_c_languages_and_ides(self):
        """Тест задания 3: проверка языков на 'C' и связанных IDE"""
        result = self.system.task3()
        
        print("\n[Тест 3] Проверка языков на 'C' и связанных IDE")
        print(f"Найдено языков: {list(result.keys())}")
        
        # Проверяем, что найдены правильные языки
        expected_languages = {"C#", "C++"}
        self.assertEqual(set(result.keys()), expected_languages)
        
        # Проверяем IDE для C#
        self.assertEqual(result["C#"], ["Visual Studio"])
        print("  ✓ C# поддерживается в Visual Studio")
        
        # Проверяем IDE для C++
        self.assertEqual(sorted(result["C++"]), ["VS Code", "Visual Studio"])
        print("  ✓ C++ поддерживается в VS Code и Visual Studio")


class TestEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""
    
    def test_empty_data(self):
        """Тест с пустыми данными"""
        print("\n[Тест 4] Проверка работы с пустыми данными")
        system = ProgrammingSystem([], [], [])
        
        # Все задачи должны возвращать пустые результаты
        self.assertEqual(system.task1(), {})
        print("  ✓ Задание 1 возвращает пустой словарь")
        
        self.assertEqual(system.task2(), [])
        print("  ✓ Задание 2 возвращает пустой список")
        
        self.assertEqual(system.task3(), {})
        print("  ✓ Задание 3 возвращает пустой словарь")
    
    def test_custom_data(self):
        """Тест с пользовательскими данными"""
        print("\n[Тест 5] Проверка с пользовательскими данными")
        # Создаем тестовые данные
        ides = [
            IDE(1, "Custom Studio"),
            IDE(2, "Test IDE")
        ]
        
        languages = [
            ProgrammingLanguage(1, "Cobra", 90, 1),
            ProgrammingLanguage(2, "Crystal", 85, 2)
        ]
        
        links = [
            LanguageIDE(1, 1),
            LanguageIDE(2, 2)
        ]
        
        system = ProgrammingSystem(ides, languages, links)
        
        # Проверяем задание 1
        task1_result = system.task1()
        self.assertEqual(list(task1_result.keys()), ["Custom Studio"])
        print("  ✓ Custom Studio найден в задании 1")
        
        # Проверяем задание 3
        task3_result = system.task3()
        self.assertEqual(sorted(task3_result.keys()), ["Cobra", "Crystal"])
        print("  ✓ Языки Cobra и Crystal найдены в задании 3")


if __name__ == "__main__":
    print("=" * 60)
    print("МОДУЛЬНОЕ ТЕСТИРОВАНИЕ - ВАРИАНТ 12")
    print("=" * 60)
    
    # Запускаем тесты с минимальным выводом unittest
    runner = unittest.TextTestRunner(verbosity=0)
    suite = unittest.TestLoader().loadTestsFromModule(__import__(__name__))
    
    # Запускаем тесты и сохраняем результат
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    if result.failures:
        print("\nПроваленные тесты:")
        for test, traceback in result.failures:
            print(f"  - {test}")
            
    if result.errors:
        print("\nТесты с ошибками:")
        for test, traceback in result.errors:
            print(f"  - {test}")
    
    print("=" * 60)