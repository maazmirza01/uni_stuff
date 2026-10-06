import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import decipher_text


def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q3_testcases = [
    # Visible Testcases (from Sample Interaction)
    ("7<@4$?!@(>-<@42@!@??'>+=@47<-<2@!@6:??4:-<??'>-<1;??",
     "the artifacts lie in paris", True),
    ("-<??'>%?-<+='>3:/@2@??4:",
     "hide in rome", True),
    ("@4??'>8>!@7<@42@!@??'>+=",
     "save the art", True),

    # Hidden Testcases - minimal case, clean two-letter result, no symbols
    ('!@"@',
     "fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603", False),

    # Hidden Testcases - swap_halves + reverse_string fully traceable, no symbols
    ('!@"@$?%?\'>(>',
     "05eb7835638bc7ad251337a7b0f1c9c9f9f0d2dc080cb4b0e821a6684157d49b", False),
    ("6:5<2@7<@4@5",
     "14a59836d9bceca4c12cc1b3cc0c6472d65d4d8aba08b93dea56a962a033bcc3", False),
    ("+='>1;1;/@/@",
     "b9340801f8ee18d2db49a28d28eb550a5be5100653e87ba369d08c3b670a7523", False),

    # Hidden Testcases - '~' (the table's only symbol-producing pair "??") interspersed with letters
    ("!@??\"@??",
     "53a793b0a71115451c7710325929f71119cae80798460d6d400193fe43674c0c", False),
    ("!@!@!@!@????????",
     "f72b5bfe9b996defd28344fcbea2966f22624d8b27558a75145342f7a2ac580d", False),
    ("<<??>;??==??9>??",
     "8cd0bc5c8c7ebd4adc54355bdbbe9becff04ae9a656aa6019e5121df3a284f52", False),

    # Hidden Testcases - repeated boundary letter 'z' ("==" -> 'z', upper end of a-z range)
    ("========",
     "2d6ccd34ad7af363159ed4bbe18c0e43c681f606877d9ffc96b62200720d7291", False),

    # Hidden Testcases - entirely symbol-producing pairs ("??" repeated -> all blanks)
    ("????????????????",
     "8b6fa01313ce51afc09e610f819250da501778ad363cba4f9e312a6ec823d42a", False),
]


@pytest.mark.parametrize("message, expected, visible", q3_testcases)
def test_q3(message, expected, visible):
    if visible:
        assert decipher_text(message) == expected
    else:
        assert hashcode(decipher_text(message)) == expected