import pytest
from app import calculate_discount


def test_calculate_discount_valid():
    assert calculate_discount(1000, 20) == 800.0
    assert calculate_discount(500, 0) == 500.0
    assert calculate_discount(100, 100) == 0.0


def test_calculate_discount_invalid_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_calculate_discount_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
