from .context import *
import pytest
from triangle import Triangle

class TestTriangle(object):
    def test_triangle_constructor_sets_length_of_3_sides(self):
        sides = [3, 4, 5]
        
        triangle = Triangle(sides)

        assert triangle.sides == sides

