import pytest
from bubble_sort import bubble_sort


@pytest.mark.parametrize("inp, out", [
    ([5, 3, 8, 4, 6], [3, 4, 5, 6, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([4, 2, 4, 1, 2], [1, 2, 2, 4, 4]),
    ([-3, 0, -1, 5, -8], [-8, -3, -1, 0, 5]),
    ([], []),
    ([42], [42]),
])
def test_bubble_sort_cases(inp, out):
    assert bubble_sort(inp) == out


def test_intentional_error():
    inp = [3, 1, 2]
    out = [1, 2, 3]
    assert bubble_sort(inp) == out