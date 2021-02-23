import pytest
import math
import pylint
@pytest.mark.parametrize("x1, x2, x3, y1, y2, expected"
, [
    (1, 2, 4, 1, 4, 10)
    ])

def test_exercise(x1, x2, x3, y1, y2, expected):
    from exercise import find_y3 
    answer = find_y3(x1, x2, x3, y1, y2)
    assert answer == pytest.approx(expected)