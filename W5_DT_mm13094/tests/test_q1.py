import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import sum_digits

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q1_testcases = [
    # Visible Testcases
    (24, 6, True),
    (0, 0, True),
    (1092, 3, True),

    # Hidden Testcases
    (5, 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False),
    (10, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (99, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (123, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    (999, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (1000, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (9876, '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False),
    (12345, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    (99999, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (100000, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (10101, '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False),
    (4444, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),
    (999999, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (123456789, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    (2147483647, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (1000000000, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False),
    (999999999999, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
]

@pytest.mark.parametrize("n, expected, visible", q1_testcases)
def test_q1(n, expected, visible):
    actual = sum_digits(n)
    if visible:
        assert actual == expected
    else:
        assert hashcode(actual) == expected


# -----------------------------------------#
# ITERATION / SHORTCUT CHECKS              #
# -----------------------------------------#

def test_q1_uses_iteration():
    """sum_digits must use at least one for/while loop."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    loops = [node for node in ast.walk(tree) if isinstance(node, (ast.For, ast.While))]
    assert loops, "sum_digits must be implemented iteratively using a for or while loop."


def test_q1_no_recursion():
    """Recursive calls to sum_digits are not allowed."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    recursive_calls = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "sum_digits"
    ]
    assert not recursive_calls, "Recursion is not allowed. Use iteration."


def test_q1_no_string_conversion():
    """Do not solve the digit problem by converting n to a string."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    forbidden = {"str"}
    calls = [
        node.func.id for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in forbidden
    ]
    assert not calls, "Do not convert n to a string. Process its digits numerically."


def test_q1_no_shortcut_builtins():
    """Reject common shortcuts that bypass the intended iterative digit processing."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    forbidden = {"sum", "map", "eval", "exec"}
    calls = [
        node.func.id for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in forbidden
    ]
    assert not calls, "Do not use sum(), map(), eval(), or exec() shortcuts."


def test_q1_no_comprehensions():
    """Comprehensions/generator expressions are not part of the intended solution."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    shortcuts = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp))
    ]
    assert not shortcuts, "Do not use comprehensions or generator expressions."


def test_q1_no_digital_root_formula_shortcut():
    """Require actual iterative digit processing rather than the modulo-9 digital-root formula."""
    import ast
    import inspect
    import q1

    source = inspect.getsource(q1.sum_digits)
    tree = ast.parse(source)

    modulo_nine = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.BinOp)
        and isinstance(node.op, ast.Mod)
        and isinstance(node.right, ast.Constant)
        and node.right.value == 9
    ]
    assert not modulo_nine, "Do not use the modulo-9 digital-root shortcut; process the digits iteratively."
