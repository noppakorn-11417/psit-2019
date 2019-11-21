"""EZ"""
def fahrenheit(value):
    """555"""
    return (value*(9/5))+32
def kelvin(value):
    """555"""
    return value+273.15
def rankine(value):
    """555"""
    return (value+273.15)*(9/5)
def celsius(value, types):
    """EZ"""
    if types == "F":
        return (value-32)*(5/9)
    elif types == "K":
        return value-273.15
    elif types == "R":
        return (value-491.67)*(5/9)
    return value
def temp_con(value, types, new_type):
    """EZ"""
    value = celsius(value, types)
    if new_type == "K":
        return kelvin(value)
    elif new_type == "F":
        return fahrenheit(value)
    elif new_type == "R":
        return rankine(value)
    return value
print("%.2f"%temp_con(float(input()), input(), input()))
