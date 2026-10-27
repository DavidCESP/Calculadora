import sys
from pathlib import Path

# Obtiene la ruta del directorio padre (un nivel arriba)
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from calculadora import sumar, restar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(2, 4) == 6
    assert sumar(2, 3) == 5


def test_restar():
    assert restar(4, 1) == 3
