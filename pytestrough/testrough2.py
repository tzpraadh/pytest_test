import pytest

def test_total_divisible_by_6(init_driver):
    assert init_driver % 6 == 0

def test_total_divisible_by_7(init_driver):
    assert init_driver % 7 == 0