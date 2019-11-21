"""nani the f_ck"""
def main(num1, num2, num3, num4):
    """result"""
    print(cal1(cal1(num1)))
    print(cal2(cal1(num1-num2)))
    print(cal3(cal1(num1+num2), cal1(num1+num3), cal2(cal1(num4**2))))
    print(cal4(cal3(cal1(num1+num2), cal1(num1-num3), cal2(cal1(num4**2))), \
    cal2(cal1(num1-num2)), cal1(cal1(cal1(cal1(cal1(num3))))), num4**8))
def cal1(num1):
    """fuction"""
    return num1*2
def cal2(num1):
    """fuction"""
    return (3*num1**4)-num1**3+(2*num1**2)+10
def cal3(num1, num2, num3):
    """fuction"""
    return (num1+num3)**2-num1*num2+num2**2
def cal4(num1, num2, num3, num4):
    """fuction"""
    return ((num1**2)+(num2**2)-(num3**2))/((num4**2)-(2*num1*num4)+2*num1)
main(float(input()), float(input()), float(input()), float(input()))
