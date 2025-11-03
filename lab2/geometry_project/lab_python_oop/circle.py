import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Circle(Figure):
    """Класс Круг"""
    
    def __init__(self, radius, color):
        self._radius = radius
        self.color = Color(color)
        self._name = "Круг"
    
    @property
    def name(self):
        return self._name
    
    def area(self):
        """Вычисление площади круга"""
        return math.pi * self._radius ** 2
    
    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {:.2f}".format(
            self.name,
            self.color.color_property,
            self._radius,
            self.area()
        )