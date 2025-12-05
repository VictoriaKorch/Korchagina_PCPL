# test_field_bdd_style.py
from field import field

class FieldExtractionBDD:
    """BDD-стиль тестирования без внешних фреймворков"""
    
    def given_sample_data(self):
        self.data = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'title': None, 'price': 1500}
        ]
        return self
    
    def when_extract_field(self, field_name):
        self.result = list(field(self.data, field_name))
        return self
    
    def when_extract_fields(self, *fields):
        self.result = list(field(self.data, *fields))
        return self
    
    def then_result_should_be(self, expected):
        assert self.result == expected, f"Ожидалось {expected}, получено {self.result}"
        return self
    
    def then_result_should_be_empty(self):
        assert self.result == [], f"Ожидался пустой список, получено {self.result}"
        return self

# Использование
def test_bdd_style():
    """BDD тесты в чистом Python"""
    print("Запуск BDD тестов...")
    
    # Сценарий 1
    (FieldExtractionBDD()
     .given_sample_data()
     .when_extract_field('title')
     .then_result_should_be(['Ковер', 'Диван для отдыха']))
    print("✓ Сценарий 1 пройден")
    
    # Сценарий 2
    (FieldExtractionBDD()
     .given_sample_data()
     .when_extract_fields('title', 'price')
     .then_result_should_be([
         {'title': 'Ковер', 'price': 2000},
         {'title': 'Диван для отдыха', 'price': 5300},
         {'price': 1500}
     ]))
    print("✓ Сценарий 2 пройден")
    
    # Сценарий 3
    (FieldExtractionBDD()
     .given_sample_data()
     .when_extract_field('nonexistent')
     .then_result_should_be_empty())
    print("✓ Сценарий 3 пройден")

if __name__ == '__main__':
    test_bdd_style()