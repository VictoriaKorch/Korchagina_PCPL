from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    """Класс Прямоугольник"""
    
    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self.color = Color(color)
        self._name = "Прямоугольник"
    
    @property
    def name(self):
        return self._name
    
    def area(self):
        """Вычисление площади прямоугольника"""
        return self._width * self._height
    
    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} площадью {:.2f}".format(
            self.name,
            self.color.color_property,
            self._width,
            self._height,
            self.area()
        )