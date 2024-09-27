import pytest
from calculator import Calculator

@pytest.fixture
def setup_calculator():
    Calculator.clear_history()

def test_addition(setup_calculator):
    assert Calculator.add(5, 3) == 8

def test_subtraction(setup_calculator):
    assert Calculator.subtract(10, 5) == 5

def test_multiplication(setup_calculator):
    assert Calculator.multiply(4, 2) == 8

def test_division(setup_calculator):
    assert Calculator.divide(9, 3) == 3

def test_divide_by_zero(setup_calculator):
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

def test_history(setup_calculator):
    Calculator.add(5, 2)
    Calculator.subtract(9, 4)
    history = Calculator.get_history()
    assert len(history) == 2
    assert history[0].result == 7
    assert history[1].result == 5

