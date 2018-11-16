import pytest
from convert import convert_units

def test_pound_kilo():
    units = convert_units(4, "pound", "kilogram")
    assert round(units, 2) == 2.16


def test_kilo_miles():
    units = convert_units(4, "kilometer", "mile")
    assert round(units, 2) == 2.48


def test_gallon_liter():
    units = convert_units(2, "gallon", "liter")
    assert round(units, 2) == 7.58


def test_fahrenheit_celsius():
    units = convert_units(75, "fahrenheit", "celsius")
    assert round(units, 2) == 23.89


def test_miles_kilo():
    units = convert_units(2, "mile", "kilometer")
    assert round(units, 2) == 3.22
