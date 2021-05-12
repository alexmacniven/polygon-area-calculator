from __future__ import annotations
from typing import Union


class Rectangle:
    """The Rectangle class."""
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height

    def __str__(self) -> str:
        """Returns a string representation of the object."""
        return f"Rectangle(width={self._width}, height={self._height})"

    def set_width(self, new_width: int):
        """Updates the object's width member."""
        self._width = new_width

    def set_height(self, new_height: int):
        """Update the object's height member."""
        self._height = new_height

    def get_area(self) -> int:
        """Returns the area of the represented shape."""
        return self._width * self._height

    def get_perimeter(self) -> int:
        """Returns the perimeter of the represented shape."""
        return 2 * self._width + 2 * self._height

    def get_diagonal(self) -> int:
        """Returns the diagonal measurement of the represented shape."""
        return (self._width ** 2 + self._height ** 2) ** .5

    def get_picture(self) -> str:
        """Returns a picture of the represented shape."""
        if self._width > 50:
            return "Too big for picture."
        return f"{'*' * self._width}\n" * self._height

    def get_amount_inside(self, shape: Union[Rectangle, Square]) -> int:
        """Returns how many copies of `shape` fit's into the represented shape."""
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    """The Square class inherits from Rectangle."""
    def __init__(self, length: int):
        super().__init__(length, length)

    def __str__(self):
        """Returns a string representation of the object."""
        return f"Square(side={self._width})"

    def set_side(self, new_length: int):
        """Updates the height and width of the represented shape."""
        self.set_height(new_length)
        self.set_width(new_length)
