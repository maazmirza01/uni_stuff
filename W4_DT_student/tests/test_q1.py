import ast
import hashlib
import inspect
import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import potion_doses


q1_testcases = [
    # Visible Testcases
    (4, 3, [1, 2, 3, 2], 0, True),
    (5, 7, [2, 7, 8, 10, 3], 3, True),

    # Hidden Testcases
    (1, 5, [5], "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (1, 5, [9], "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a", False),
    (3, 4, [6, 2, 4], "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35", False),
    (6, 8, [1, 3, 8, 9, 10, 12], "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a", False),
    (5, 1, [1, 1, 1, 1, 1], "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (5, 1, [2, 3, 4, 5, 6], "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d", False),
    (4, 10, [25, 2, 10, 11], "e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb", False),
    (7, 25, [25, 24, 1, 12, 8, 19, 3], "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", False),
    (8, 12, [4, 17, 9, 12, 15, 7, 11, 13], "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d", False),
    (10, 6, [6, 6, 7, 6, 8, 6, 9, 6, 10, 6], "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a", False),
    (9, 3, [3, 4, 5, 6, 7, 8, 9, 10, 11], "2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3", False),
    (25, 13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918", False),
    (6, 20, [20, 18, 21, 19, 22, 17], "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35", False),
]


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def _uses_iteration(function):
    tree = ast.parse(inspect.getsource(function))
    return any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))


@pytest.mark.parametrize(
    "hurdle_count,max_jump_height,hurdle_heights,expected,visible",
    q1_testcases,
)
def test_q1(monkeypatch, hurdle_count, max_jump_height, hurdle_heights, expected, visible):
    values = iter(hurdle_heights)
    calls = 0

    def fake_input(prompt=""):
        nonlocal calls
        calls += 1
        try:
            return str(next(values))
        except StopIteration:
            pytest.fail("The function called input() more than hurdle_count times.")

    monkeypatch.setattr("builtins.input", fake_input)

    result = potion_doses(hurdle_count, max_jump_height)

    assert calls == hurdle_count, (
        f"The function must read exactly {hurdle_count} hurdle heights using input()."
    )

    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected


def test_q1_uses_iteration():
    assert _uses_iteration(potion_doses), "Use iteration in potion_doses()."
