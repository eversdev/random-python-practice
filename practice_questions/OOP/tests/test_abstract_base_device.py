import pytest
from app.abstract_base_device import Device, Phone, Laptop, boot_device
from unittest.mock import patch


def test_abstract_base():
    """Test that instantiating Device raises TypeError."""
    with pytest.raises(TypeError):
        Device()


def test_phone_instantiation():
    """Test that a Phone instance can be created successfully."""
    p1 = Phone()
    assert isinstance(p1, Phone)



def test_laptop_instantiation():
    """Test that a Laptop instance can be created successfully."""
    l1 = Laptop()
    assert isinstance(l1, Laptop)


@patch("app.abstract_base_device.Phone.start")
def test_boot_device(mock_boot_device):
    p = Phone()
    boot_device(p)
    mock_boot_device.assert_called_once()

