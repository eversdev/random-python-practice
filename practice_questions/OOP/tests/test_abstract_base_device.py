from unittest.mock import patch

import pytest
from app.abstract_base_device import Device, Laptop, Phone, boot_device

# Beginning of Structural tests


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


# Beginning of Behavioural tests


def test_phone_start(capfd):
    """Verify Phone.start() prints 'Dial a number'."""
    p = Phone()
    p.start()
    out, _ = capfd.readouterr()
    assert "Dial a number" in out


def test_laptop_start(capfd):
    """Verify Laptop.start() prints 'Power on!'."""
    l1 = Laptop()
    l1.start()
    out, _ = capfd.readouterr()
    assert "Power on!" in out


def test_boot_device_start_phone(capfd):
    """Verify that a Phone instance prints 'Dial a number' when booted."""
    p = Phone()
    boot_device(p)
    out, _ = capfd.readouterr()
    assert "Dial a number" in out


def test_boot_device_start_laptop(capfd):
    """Verify that a Laptop instance prints 'Power on!' when booted."""
    l1 = Laptop()
    boot_device(l1)
    out, _ = capfd.readouterr()
    assert "Power on!" in out
