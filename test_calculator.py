# test_calculator.py
from calculator import add, subtract, multiply
 
 
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
 
 
def test_subtract():
    assert subtract(5, 1) == 4
 
 
def test_multiply():
    assert multiply(4, 5) == 20





import pytest
from calculator import divide
 
 
def test_divide():
    assert divide(10, 2) == 5
 
 
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)