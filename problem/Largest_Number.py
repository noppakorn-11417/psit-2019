"""despacito"""
def main(num1, num2, num3):
    """despacito"""
    case1, case2, case3 = num1+num2+num3, num1+num3+num2, num2+num1+num3
    case4, case5, case6 = num2+num3+num1, num3+num2+num1, num3+num1+num2
    print(int(larg(case6, larg(case5, larg(case4, larg(case3, larg(case2, case1)))))))
def larg(value1, value2):
    """i can fly"""
    if value2 >= value1:
        value1 = value2
    return value1
main(input(), input(), input())
