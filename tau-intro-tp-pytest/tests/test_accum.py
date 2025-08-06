import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from stuff.accum import Accumulator


@pytest.fixture
def accum():
    """Fixture to create a new Accumulator instance for each test."""
    return Accumulator()
@pytest.mark.accumulator
def test_accumulator_init(accum):
    
    assert accum.count == 0
@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    
    accum.add(1)
    assert accum.count == 1
@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    
    accum.add(3)
    assert accum.count == 3
@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    
    accum.add(1)
    accum.add(1)
    assert accum.count == 2
@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10
    assert accum.count == 0