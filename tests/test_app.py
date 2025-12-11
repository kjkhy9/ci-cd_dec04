import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import mult

def test_mult():
    assert mult(5,6) == 30

def test_mult2():
    assert mult(5,6) != 29
