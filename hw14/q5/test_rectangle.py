import pytest
from rectangle import Rectangle

def test_area():
    rectangle = Rectangle(4, 5)
    assert rectangle.area() == 20

def test_perimeter():
    rectangle = Rectangle(4, 5)
    assert rectangle.perimeter() == 18

def test_invalid_dimensions():
    with pytest.raises(ValueError, match="Dimensions must be positive"):
        Rectangle(-1, 5)
    with pytest.raises(ValueError, match="Dimensions must be positive"):
        Rectangle(4, -5)
    with pytest.raises(ValueError, match="Dimensions must be positive"):
        Rectangle(-1, -5)