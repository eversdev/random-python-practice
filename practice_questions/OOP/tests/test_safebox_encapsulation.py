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


def test_instance_has_one_attribute():
    s1 = SafeBox()
    assert len(s1.__dict__) == 1


@patch("app.safebox_encapsulation.input")
def test_set_code_input_too_long(mock_obj):
    mock_obj.return_value = "12345"
    s1 = SafeBox()
    result = s1.set_code()
    assert result == "The code you entered exceeds 4 digits."


@patch("app.safebox_encapsulation.input")
def test_set_code_input_too_short(mock_obj):
    mock_obj.return_value = "123"
    s1 = SafeBox()
    result = s1.set_code()
    assert result == "The code you entered is less than 4 digits."


@patch("app.safebox_encapsulation.input")
def test_set_code_input_valid_length(mock_obj):
    mock_obj.return_value = "1234"
    s1 = SafeBox()
    result = s1.set_code()
    assert result == "You have entered 1234 as your code."
    assert s1._SafeBox__code == 1234


def test_check_code_with_correct_code():
    s1 = SafeBox()
    s1._SafeBox__code = 1234
    assert s1.check_code(1234) == "Code entered correctly."


def test_check_code_with_wrong_code():
    s1 = SafeBox()
    s1._SafeBox__code = 1234
    assert s1.check_code(0o123) == "Incorrect code entered."


def test_check_code_with_non_string_input():
    s1 = SafeBox()
    s1._SafeBox__code = 1234
    result = s1.check_code(1234)
    assert isinstance(result, str)
