import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import break_loop


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


q4_testcases = [
    # Visible Testcases (from Sample Interaction)
    (4, 30, "Timeline stabilized!", True),
    (19, 60, "Intervention successful!", True),
    (2, 25, "Loop remains unbroken!", True),
    (119393, 200000, "Stable state found!", True),

    # Hidden Testcases - limit boundary
    (100, 50,
     "aecff47548e03c771c749e1f03a050a41a6bd01d2147ba7ea3c858aecd4df9e6", False),  # exceeds limit immediately
    (1, 5,
     "aecff47548e03c771c749e1f03a050a41a6bd01d2147ba7ea3c858aecd4df9e6", False),  # small start, tight limit
    (52, 52,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),  # signature == limit exactly (must NOT trigger unbroken)

    # Hidden Testcases - divisible by 7
    (7, 100,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),  # immediate
    (14, 100,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),  # immediate
    (10, 10000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),  # reached after multiple iterations

    # Hidden Testcases - range 40 to 50 (inclusive) boundaries
    (40, 100,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),  # lower boundary
    (50, 100,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),  # upper boundary
    (39, 100,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),  # just below, must continue iterating
    (51, 100,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),  # just above, must continue iterating

    # Hidden Testcases - "Stable" state with score >= 100
    (9999, 50000,
     "4d5be766598d6493a89592dba14ba0e741b418c933490f4f86b3a59019226b25", False),  # Stable, score=105, direct match
    (6999, 50000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),  # Stable, score=90 (<100), must continue
    (67899, 100000,
     "4d5be766598d6493a89592dba14ba0e741b418c933490f4f86b3a59019226b25", False),  # Stable, score EXACTLY 100
    (36999, 100000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),  # Stable, score EXACTLY 99 (just below)

    # Hidden Testcases - Critical state (divisible by both 3 and 5)
    (15, 1000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),
    (30, 1000,
     "525202c66f1a3d646c03ac8e04a40b5961b0b5b76e2f3e2b421c3b26be1a4bcb", False),

    # Hidden Testcases - general/miscellaneous
    (1, 1000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),
    (9973, 50000,
     "ebaede559bdc18951b90e9f0ffb468beead3d49b1906f033fe4f4c7988c8b536", False),
]


@pytest.mark.parametrize("signature, limit, expected, visible", q4_testcases)
def test_q4(signature, limit, expected, visible):
    if visible:
        assert break_loop(signature, limit) == expected
    else:
        assert hashcode(break_loop(signature, limit)) == expected