from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат (наследуется от Прямоугольника)"""
    
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self._name = "Квадрат"
    
    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return "{} {} цвета со стороной {} площадью {:.2f}".format(
            self.name,
            self.color.color_property,
            self._width,
            self.area()
        )