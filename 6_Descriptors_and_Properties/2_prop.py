class RectangleWithProperties:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive")

rect_with_props = RectangleWithProperties(5, 10)
print(rect_with_props.width)  # Output: 5

rect_with_props.width = 8
print(rect_with_props.width)  # Output: 8

rect_with_props.width = -2  # Raises ValueError: Width must be positive
