import pytest
import hashlib
import ast
import inspect
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import clean_message

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q1_testcases = [
    # Visible Testcases
    ('hello#!', 'hell!', True),
    ('abc##d', 'ad', True),
    ('##abc', 'abc', True),
    ('a##bc', 'bc', True),
    ('abc###', '', True),
    ('campuss## life', 'campu life', True),

    # Hidden Testcases
    ('a#', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('#', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('####', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('ab#c', 'f45de51cdef30991551e41e882dd7b5404799648a0a00753f44fc966e6153fc1', False),
    ('a#b#c#', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', False),
    ('hello world', 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9', False),
    ('12#34', '5d389f5e2e34c6b0bad96581c22cee0be36dcf627cd73af4d4cccacd9ef40cc3', False),
    ('a b#c', 'a9573e0ed68e10d0d61a596168c094f8cbcbb7380cd9ef6bce3fb34cc167e219', False),
    ('abc####d', '18ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4', False),
    ('Python###!', '96b1b37da75872ee1a9261ac614b76e44e773a16fef89a8818b19b55fff9f9ed', False),
    ('##a#b', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', False),
    ('x##y##z', '594e519ae499312b29433b7dd8a97ff068defcba9755b6d5d00e84c524d67b06', False),
    ('message#', '9be41bb5203e37dc808c3aca17f21daccdd293fadf8debe4dd0cba835183da41', False),
    ('a###b###c', '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6', False),
]

@pytest.mark.parametrize("draft_message, expected, visible", q1_testcases)
def test_q1(draft_message, expected, visible):
    if visible:
        assert clean_message(draft_message) == expected
    else:
        assert hashcode(clean_message(draft_message)) == expected

def test_q1_uses_iteration():
    source = inspect.getsource(clean_message)
    tree = ast.parse(source)
    assert any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree)), \
        "clean_message must be implemented iteratively using a for or while loop."
