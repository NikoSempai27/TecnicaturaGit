class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def colo(self, color):
        self._color = color

    def __str__(self):
        return f'Color [Color: {self._color} ]'
