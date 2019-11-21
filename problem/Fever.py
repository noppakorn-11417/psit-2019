"""EZ"""
def main(number):
    """555"""
    if number < 38:
        return "No Fever"
    elif 38 <= number < 39:
        return "Mild Fever"
    elif 39 <= number < 40:
        return "High Fever"
    else:
        return "Very High Fever"
print(main(float(input())))
