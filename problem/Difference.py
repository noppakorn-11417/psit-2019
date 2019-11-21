"""fc inw bas"""
def main(num1=0, num2=0):
    """fc inw bas"""
    cal1 = set([int(input()) for _ in range(num1)])
    cal2 = set([int(input()) for _ in range(num2)])
    return cal1-cal2
print(*sorted(list(main(int(input()), int(input())))))
