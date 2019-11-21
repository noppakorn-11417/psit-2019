"""despacito"""
def main(num1, num2, num3, num4):
    """despacito"""
    cal = (num1+num4)-(num1+num4)*(num3/100)
    if cal < (num1*((100-num3*(num1 >= num2))/100)):
        print("Yes", "%.3f"%abs(cal-(num1*((100-num3*(num1 >= num2))/100))))
    elif cal > (num1*((100-num3*(num1 >= num2))/100)):
        print("No", "%.3f"%abs(cal-(num1*((100-num3*(num1 >= num2))/100))))
    else:
        print("Yes")
main(float(input()), float(input()), float(input()), float(input()))
