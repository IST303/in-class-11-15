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

pound = 'pound'
kilogram = 'kilogram'
mile = 'mile'
kilometer = 'kilometer'
fahrenheit = 'fahrenheit'
celsius = 'celsius'
gallon = 'gallon'
liter = 'liter'
    
test_case = {
(1, pound, kilogram, 0.45),
(1, mile, kilometer, 1.61),
(1, fahrenheit, celsius, -17.22),
(1, gallon, liter, 3.79),
(6, pound, kilogram, 2.72),
(4, mile, kilometer, 6.44),
(90, fahrenheit, celsius, 32.22),
(8, gallon, liter, 30.28)
}

@pytest.mark.parametrize('amount,current_unit,converted_unit,expected', test_case)
def test_convert_units(amount, current_unit, converted_unit, expected):
    return_value = convert_units(amount, current_unit, converted_unit)
    assert round(return_value,2) == expected
    

invalid_test_case = {
(0.45, kilogram, pound, 1),
(1.16, kilometer, mile, 1),
(1, pound, 'abcdeddkdjkd', 0.45),
}

@pytest.mark.parametrize('amount,current_unit,converted_unit', invalid_test_case)
def raise_test_convert_units(amount, current_unit, converted_unit, expected):
    with pytest.raises(Exception):
        convert_units(amount, current_unit, converted_unit)
