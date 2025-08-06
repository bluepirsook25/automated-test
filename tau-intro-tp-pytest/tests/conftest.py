import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from stuff.accum import Accumulator 


@pytest.fixture
def accum():
    """Fixture to create a new Accumulator instance for each test."""
    yield Accumulator()
    print("Done with the test!")

@pytest.fixture
def accum2():
    """Fixture to create a new Accumulator instance for each test."""
    return Accumulator()    