import pytest

from tests.Calculator import Calculator



class TestCalc:
    def test_adding_success(self):
        assert Calculator.adding(self, 5, 5) == 10

    def test_multiply_success(self):
        assert Calculator.multiply(self, 5, 5) == 25

    def test_division_success(self):
        assert Calculator.division(self, 10, 5) == 2
        

    def test_subtraction_success(self):
        assert Calculator.subtraction(self, 5, 2) == 3

