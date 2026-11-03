import builtins
import hashlib
import os
import sys
from copy import deepcopy

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import q1


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def run_main(patch, capsys, input_lines):
    """Run q1.main() with fake input and a counted print.

    Returns (number of input() calls, number of print() calls, printed text).
    Accepts both input() and input("prompt"); the prompt text is ignored.
    """
    input_iterator = iter(input_lines)
    input_calls = []
    output_calls = []
    original_print = builtins.print

    def fake_input(prompt=""):
        input_calls.append(prompt)
        try:
            return next(input_iterator)
        except StopIteration:
            pytest.fail("main() requested too many input lines.")

    def count_print(*args, **kwargs):
        output_calls.append((args, kwargs))
        return original_print(*args, **kwargs)

    patch.setattr(builtins, "input", fake_input)
    patch.setattr(builtins, "print", count_print)
    q1.main()
    return len(input_calls), len(output_calls), capsys.readouterr().out


q1_testcases = [
    # Visible Testcases
    ([[1, 2, 0, 4, 8], [4, 5, 6, 5, 9], [7, 0, 9, 9, 3], [9, 8, 7, 6, 2]], [[0, 0, 0, 0, 0], [4, 0, 0, 5, 9], [0, 0, 0, 0, 0], [9, 0, 0, 6, 2]], True),
    ([[1, 2, 3, 8], [4, 5, 6, 9], [7, 0, 9, 10]], [[1, 0, 3, 8], [4, 0, 6, 9], [0, 0, 0, 0]], True),
    ([[1, 0], [1, 1], [3, 4]], [[0, 0], [1, 0], [3, 0]], True),
    ([[0, 1, 3], [1, 3, 6], [6, 9, 9], [3, 7, 2]], [[0, 0, 0], [0, 3, 6], [0, 9, 9], [0, 7, 2]], True),
    ([[1, 1, 1, 1], [5, 0, 4, 4], [0, 5, 9, 6], [2, 0, 4, 1], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], True),

    # Hidden Testcases
    ([[7]], 'f61d0f7aee2b3c93c7c0efdf268606eda07dff009674a008e50188bbd9822224', False),
    ([[0]], 'db407f11d7ede59abaab0e98e097ff2dae10a048207b801745d7199ef19c2387', False),
    ([[3, 0, 4, 5, 6, -1]], 'f3f029acd07e32b1cc2ca826dc4cef73d043e6c0856831fa9e6d3a6181b009a7', False),
    ([[2], [4], [-1], [0], [9], [3]], '2199248749e9493585cea9e3269f3934d2f0f579258b3e94825feb905c11fdf2', False),
    ([[-100, 1, 2, 3, 4], [9, -5, 8, 7, 100]], 'a258fb7037fcdf0fc0c33669b995cb06de7f00d204ce0341298cfa74521111ff', False),
    ([[1, 2, 3, 4, 0], [9, 8, 7, 6, 5]], 'd62308aff0e080537c782bf0df961d1780e21df1b56945bf2744d4b270654184', False),
    ([[1, 0], [2, 3], [0, 5], [6, 7], [8, 9]], '18c36fe1b2d17e83a39ddd3d45116c678065709510bf95051f2d3dc30e576368', False),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 [21, 22, 23, 0, 25, 26, 27, 28, 29, 30],
 [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
 [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
 [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
 [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
 [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
 [81, 82, 83, 84, 85, 86, 87, 0, 89, 90],
 [91, 92, 93, 94, 95, 96, 97, 98, 99, 1]], '72ed622ecad3c49792838f3be35a98a7d65ee2b5da9a57ca09adb9d9b0d98e05', False),
    ([[0, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 0]], 'cf3e232f73dbadbfe08f71d1b178c4327feeb35a22e24c589f7982c435cd32fd', False),
    ([[-20, -19, -18, -17],
 [-16, -15, -14, -13],
 [-12, -11, -10, -9],
 [-8, -7, -6, -5],
 [-4, -3, -2, -1],
 [-50, 1, 2, 3],
 [4, 5, 6, 7]], '32f744d834408f135316ef0ca668793adec321207c701d6cb274e93fd8d12770', False),
]


@pytest.mark.parametrize("matrix, expected, visible", q1_testcases)
def test_q1_set_zeros_and_main(matrix, expected, visible, monkeypatch, capsys):
    # Check set_zeros() independently: the original matrix must remain unchanged.
    original_matrix = deepcopy(matrix)
    result = q1.set_zeros(matrix)
    assert capsys.readouterr().out == "", "set_zeros() must not print."
    assert matrix == original_matrix, "set_zeros() must not modify the input matrix."
    assert isinstance(result, list) and all(isinstance(row, list) for row in result), (
        "set_zeros() must return a nested list."
    )
    assert result is not matrix, "set_zeros() must return a new matrix."
    if visible:
        assert result == expected, "set_zeros() returned the wrong matrix."
    else:
        assert hashcode(result) == expected, "set_zeros() returned the wrong matrix."

    rows, columns = len(original_matrix), len(original_matrix[0])
    input_lines = [f"{rows} {columns}"] + [" ".join(map(str, row)) for row in original_matrix]

    # Run 1: replace set_zeros temporarily to confirm that main() constructs and
    # passes a 2D list of integers, and prints the returned value once.
    received_matrices = []
    marker_result = [[123456789, -123456789]]

    def fake_set_zeros(grid):
        received_matrices.append(deepcopy(grid))
        return marker_result

    with monkeypatch.context() as patch:
        patch.setattr(q1, "set_zeros", fake_set_zeros)
        input_count, print_count, printed = run_main(patch, capsys, input_lines)

    assert input_count == len(input_lines), (
        "main() must read the dimensions and every matrix row."
    )
    assert received_matrices == [original_matrix], (
        "main() must call set_zeros() exactly once with a nested list of integers."
    )
    assert print_count == 1, "main() must print the matrix with one print() call."
    assert printed == str(marker_result) + "\n", (
        "main() must print the matrix returned by set_zeros()."
    )

    # Run 2: run main() with the real set_zeros to verify its printed result.
    with monkeypatch.context() as patch:
        input_count, print_count, printed = run_main(patch, capsys, input_lines)

    assert input_count == len(input_lines), "Incorrect number of input() calls."
    assert print_count == 1, "main() must print the matrix with one print() call."
    assert printed.endswith("\n") and printed.count("\n") == 1, (
        "main() must print the complete matrix as one list on one line."
    )
    if visible:
        assert printed == str(expected) + "\n", "main() printed an incorrect matrix."
    else:
        assert hashcode(printed[:-1]) == expected, "main() printed an incorrect matrix."
