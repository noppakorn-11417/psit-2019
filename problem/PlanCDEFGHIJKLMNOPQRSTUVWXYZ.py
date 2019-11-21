"""pair"""
def main(option, num1, num2, num3):
    """buble sort"""
    if num2 >= num1:
        num1, num2, num3 = num2, num1, num3
    if num3 >= num2:
        num1, num2, num3 = num1, num3, num2
    if num2 >= num1:
        num1, num2, num3 = num2, num1, num3
    if option == "Ascend":
        num1, num2, num3 = num3, num2, num1
    print("%.2f, %.2f, %.2f"%(num1, num2, num3))
main(input(), float(input()), float(input()), float(input()))
