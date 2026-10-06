import pytest
import hashlib
import io
import contextlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import dorothy_hourglass


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def run_and_capture(n):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        dorothy_hourglass(n)
    return buf.getvalue()


q2_testcases = [
    # Visible Testcases (from Sample Interaction)
    (5, "*********\n +++++++\n  ?????\n   $$$\n    #\n   $$$\n  ?????\n +++++++\n*********\n", True),
    (1, "*\n", True),
    (12, "n is out of range!\n", True),

    # Hidden Testcases - valid n, full range coverage (2 through 9, since 1/5/10 are visible or already derived)
    (2,
     "824926758415fe4ae2a8ede8d0a15d7515754262f82f2352976cc26bf6a7f499", False),
    (3,
     "b0cfded4ec43c4e84a35ed77449f89d2eb3bd78bc685bdc4fb5983ac3fe1d36b", False),
    (4,
     "7d3e665bbdc7fd76c250f5c85732b7926ef2106c3227cb436bc39e99f71269b5", False),
    (6,
     "ec3b1e9ca5ca7939f73fc82748d6f67cb4800dd42c46e46e7a634279b389b51b", False),
    (7,
     "e01d41aaf80b6a80e02bc914a41303bfd4d10d6262efc2e7ef0881a2f766844e", False),
    (8,
     "95c7e984315c5e2668b4a4d69cfc124e30fe03fa05a648997c9c0755f85b0bb6", False),
    (9,
     "890bb8389d7e3f8f5d8ba59f1c7edf228358e66222e3c6dff11863f0fcdf2c04", False),
    (10,
     "78f68f2154f06afeca2536716018b7ea2b4f43c5164e736893043e86c27929e7", False),

    # Hidden Testcases - invalid n, boundary and extreme cases
    (0,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
    (-1,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
    (-5,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
    (11,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
    (15,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
    (100,
     "df08553bfc7afdbe88c43d9bab27e6730dc71531970d0a1ad45cd1f223f22e5c", False),
]


@pytest.mark.parametrize("n, expected, visible", q2_testcases)
def test_q2(n, expected, visible):
    captured = run_and_capture(n)
    if visible:
        assert captured == expected
    else:
        assert hashcode(captured) == expected