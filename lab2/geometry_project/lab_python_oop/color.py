class Color:
    """Класс Цвет фигуры"""
    
    def __init__(self, color):
        self._color = color
    
    @property
    def color_property(self):
        """Свойство для получения цвета"""
        return self._color
    
    @color_property.setter
    def color_property(self, value):
        """Сеттер для цвета"""
        self._color = value