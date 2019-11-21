"""psit"""
def main(num1, num2, gcd):
    """prime nnumber"""
    for i in range(1, max(num1, num2)+1):
        if num1%i == 0 and num2%i == 0:
            gcd.add(i)
    print(max(gcd))
main(int(input()), int(input()), set())
