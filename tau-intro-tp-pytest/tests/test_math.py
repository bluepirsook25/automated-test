import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
@pytest.mark.math

def test_one_plus_one():
    assert 1 + 1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)

#Multiplication test ideas:
#two positive integers
#identify :multiply by 1
#zero: multiply by 0
#positive by negative
#negative by negative
#float
products =[
    (2,3,6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
    
]
@pytest.mark.math
@pytest.mark.parametrize("a, b, product",  products)
def test_multiply(a, b, product):
    assert a * b == product 
    
