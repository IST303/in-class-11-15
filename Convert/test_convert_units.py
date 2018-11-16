import pytest


KG_IN_1_POUND = 0.54
KM_IN_1_MILE = 1.61
LITER_IN_1_GALLON = 3.79

CONVERSION_MAP = {('fahrenheit', 'celsius'): lambda f: 5 / 9 * (f - 32),
                  ('celsius', 'fahrenheit'): lambda c: c * 9 / 5 + 32,
                  ('pound', 'kilogram'): lambda p: p * KG_IN_1_POUND,
                  ('kilogram', 'pound'): lambda k: k / KG_IN_1_POUND,
                  ('mile', 'kilometer'): lambda k: k * KM_IN_1_MILE,
                  ('kilometer', 'mile'): lambda m: m / KM_IN_1_MILE,
                  ('gallon', 'liter'): lambda g: g * LITER_IN_1_GALLON,
                  ('liter', 'gallon'): lambda l: l / LITER_IN_1_GALLON}


def convert_units(amount, current_unit, converted_unit):
    return CONVERSION_MAP.get((current_unit, converted_unit))(amount)



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

