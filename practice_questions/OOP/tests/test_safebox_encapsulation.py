from unittest.mock import patch

from app.safebox_encapsulation import SafeBox

# import pytest


def test_safebox_instantiation():
    s1 = SafeBox()
    assert isinstance(s1, SafeBox)


@patch("app.safebox_encapsulation.input")
def test_code_is_private(mock_obj):
    mock_obj.return_value = "1234"
    s1 = SafeBox()
    s1.set_code()
    assert s1._SafeBox__code == 1234


@patch("app.safebox_encapsulation.input")
def test_set_code_returns_str(mock_obj):
    mock_obj.return_value = "1234"
    s1 = SafeBox()
    assert isinstance(s1.set_code(), str)


@patch("app.safebox_encapsulation.input")
def test_check_code_returns_str(mock_obj):
    mock_obj.return_value = "1234"
    s1 = SafeBox()
    s1.set_code()
    assert isinstance(s1.check_code("1234"), str)
