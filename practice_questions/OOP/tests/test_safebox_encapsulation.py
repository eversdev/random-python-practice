import pytest
from app.safebox_encapsulation import SafeBox


def test_safebox_instantiation():
    s1 = SafeBox()
    assert isinstance(s1, SafeBox)
