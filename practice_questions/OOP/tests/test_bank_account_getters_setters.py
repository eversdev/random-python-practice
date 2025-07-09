import pytest
from app.bank_account_getters_setters import Account


# === Instance Creation ===
def test_account_instance_creation():
    """Test whether an Account instance can be instantiated correctly"""
    a1 = Account("John", 500)
    assert a1.name == "John" and a1.get_balance() == 500


# === String Representation ===
def test_str_method():
    """Test that the __str__ method returns the expected string format."""
    a1 = Account("John", 500)
    assert str(a1) == f"{a1.name} is an object of the Account class."


# === Balance Accessors ===
def test_get_balance():
    """Test that get_balance gets the correct balance of an instance you call the method on"""
    a1 = Account("Jane", 300)
    assert a1.get_balance() == 300


def test_set_balance():
    """Test set_balance to update correctly when given a valid input"""
    a1 = Account("John", 500)
    a1.set_balance(200)
    assert a1.get_balance() == 200


def test_account_methods_callable():
    """Test that set_balance can be called without errors."""
    a1 = Account("Jane", 300)
    a1.set_balance(300)
    assert a1.get_balance() == 300


# === Balance Input Validation ===
def test_set_balance_accepts_numeric_string():
    """Test that set_balance accepts strings that can be converted to ints."""
    a1 = Account("Jane", 300)
    a1.set_balance("1000")
    assert a1.get_balance() == 1000


def test_set_balance_raises_exception():
    """Test set_balance to see if it raises exception"""
    a1 = Account("John", 500)
    with pytest.raises(ValueError):
        a1.set_balance("abc")
    assert a1.get_balance() == 500


def test_set_balance_edge_cases():
    """Test set_balance behaviour with negative, zero and very large balances."""
    a1 = Account("Jane", 300)

    a1.set_balance(0)
    assert a1.get_balance() == 0

    a1.set_balance(-1)
    assert a1.get_balance() == -1

    a1.set_balance(1000000)
    assert a1.get_balance() == 1000000
