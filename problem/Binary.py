"""psit"""
def main(number, base2=""):
    """prime nnumber"""
    while True:
        base2 += str(number%2)
        number //= 2
        if number == 0:
            return print(base2[::-1])
main(int(input()))
