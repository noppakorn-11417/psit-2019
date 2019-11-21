"""pair"""
def main(num1, num2, text):
    """we will rock you"""
    return print("%30i"%num1), print("%030i"%num1), print("%.2f"%num2), print("%.12f"%num2), \
    print("%40s"%text)
main(int(input()), float(input()), input())
