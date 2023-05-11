class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value < 0:
            self.invalid_dimensions()
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            self.invalid_dimensions()
        self._width = value

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def invalid_dimensions(self):
        raise ValueError("Dimensions must be positive")
