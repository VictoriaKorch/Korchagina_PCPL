import unittest
from field import field

class TestFieldTDD(unittest.TestCase):
    
    def setUp(self):
        self.sample_data = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'title': None, 'price': 1500},
            {'color': 'red'}
        ]
    
    def test_single_field_extraction(self):
        """Тест извлечения одного поля"""
        result = list(field(self.sample_data, 'title'))
        expected = ['Ковер', 'Диван для отдыха']
        self.assertEqual(result, expected)
    
    def test_multiple_fields_extraction(self):
        """Тест извлечения нескольких полей"""
        result = list(field(self.sample_data, 'title', 'price'))
        expected = [
            {'title': 'Ковер', 'price': 2000},
            {'title': 'Диван для отдыха', 'price': 5300},
            {'price': 1500}
        ]
        self.assertEqual(result, expected)
    
    def test_empty_args_raises_error(self):
        """Тест вызова без аргументов"""
        with self.assertRaises(ValueError):
            list(field(self.sample_data))
    
    def test_none_values_handling(self):
        """Тест обработки None значений"""
        result = list(field(self.sample_data, 'color'))
        expected = ['green', 'black', 'red']
        self.assertEqual(result, expected)
    
    def test_non_existent_field(self):
        """Тест несуществующего поля"""
        result = list(field(self.sample_data, 'non_existent'))
        self.assertEqual(result, [])
    
    def test_mixed_valid_invalid_fields(self):
        """Тест смеси валидных и невалидных полей"""
        data = [{'a': 1}, {'b': 2}, {'a': 3, 'b': 4}]
        result = list(field(data, 'a', 'b'))
        expected = [{'a': 1}, {'b': 2}, {'a': 3, 'b': 4}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()