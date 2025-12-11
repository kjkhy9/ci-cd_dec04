import sys
import math
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (add, sub, mult, div, sqr, sqrt, log, sin, cos, percentage)

# --------------------
# Basic operations
# --------------------
def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mult():
    assert mult(4, 5) == 20

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(5, 0)

# --------------------
# Advanced operations
# --------------------
def test_sqr():
    assert sqr(4) == 16

def test_sqrt():
    assert sqrt(9) == 3

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_log_default_base():
    assert log(math.e) == pytest.approx(1.0)

def test_log_custom_base():
    assert log(8, 2) == 3

def test_log_invalid_value():
    with pytest.raises(ValueError):
        log(0)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(10, 1)

def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(0) == 1

def test_percentage():
    assert percentage(50, 200) == 25

def test_percentage_div_zero():
    with pytest.raises(ValueError):
        percentage(10, 0)
