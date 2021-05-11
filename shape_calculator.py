from __future__ import annotations
from typing import Union


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width: int = width
        self._height: int = height

    def set_width(self, new_width: int):
        pass

    def set_height(self, new_height: int):
        pass

    def get_perimeter(self) -> int:
        pass

    def get_diagonal(self) -> int:
        pass

    def get_picture(self) -> str:
        pass

    def get_amount_inside(self, shape: Union[Rectangle, Square]) -> int:
        pass


class Square(Rectangle):
    def __init__(self, length: int):
        self.set_height(length)
        self.set_width(length)

    def set_side(self, new_length: int):
        self.set_height(new_length)
        self.set_width(new_length)
