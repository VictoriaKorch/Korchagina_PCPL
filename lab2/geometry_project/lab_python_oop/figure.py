from abc import ABC, abstractmethod

class Figure(ABC):
    """Абстрактный класс Геометрическая фигура"""
    
    @property
    @abstractmethod
    def name(self):
        """Абстрактное свойство для имени фигуры"""
        pass
    
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади"""
        pass
    
    def __repr__(self):
        """Метод repr для вывода информации о фигуре"""
        return "{} {} цвета площадью {:.2f}".format(
            self.name, 
            self.color.color_property, 
            self.area()
        )