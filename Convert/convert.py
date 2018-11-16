def convert_units(amount, current_unit, converted_unit):
    global num2
    if current_unit == 'pound' and converted_unit == 'kilogram':
        num2 = 0.54*amount
    elif current_unit == 'mile' and converted_unit == 'kilometer':
        num2 = 1.61*amount
    elif current_unit == 'fahrenheit' and converted_unit == 'celsius':
        num2 = (5/9)*(amount-32)
    elif current_unit == 'gallon' and converted_unit == 'liter':
        num2 = 3.79* amount
    elif current_unit == 'kilogram' and converted_unit == 'pound':
        num2 = amount/0.54
    elif current_unit == 'kilometer' and converted_unit == 'mile':
        num2 = amount/1.61
    elif current_unit == 'celsius' and converted_unit == 'fahrenheit':
        num2 = (9/5)*amount+32
    elif current_unit == 'liter' and converted_unit == 'gallon':
        num2 = amount / 3.79
    return num2
