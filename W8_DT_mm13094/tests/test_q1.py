import hashlib

import os
import sys

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import sum67


def hashcode(n):
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


q1_testcases = [
    ([1, 2, 2], 5, True),
    ([4, 2, 2, 6, 99, 99, 7], 8, True),
    ([9, 1, 6, 7, 0], 10, True),
    ([6, 7], 0, True),
    ([6, 6, 7, 7], 7, True),
    ([1, 1, 6, 4, 5, 8, 0, 7, 2], 4, True),
    ([6, 7, 1, 2, 3, 7], 13, True),
    ([1, 2, 3, 6, 7, 4, 5], 15, True),
    ([], 0, True),
    ([1, 2, 3, 6, 99, 99, 7, 4, 5], 'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb', False),
    ([6, 7, 6, 7, 6, 7], '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ([5, 6, 1, 7, 6, 3, 7], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False),
    ([1, 2, 6, 7, 1, 2, 3], '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', False),
    ([6, 7, 6, 7, 6, 7, 1, 2, 3], 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    ([0, 1, 6, 7, 2], '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False),
    ([6, 7, 7, 6, 7], '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),
    ([1, 2, 6, 7, 6, 7, 8], '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8', False)
]


@pytest.mark.parametrize("lst, result, testcase", q1_testcases)
def test_question1(lst, result, testcase):
    actual = sum67(lst)
    if testcase:
        assert actual == result
    else:
        assert hashcode(actual) == result