"""psit week3"""
def main(num, count):
    """i love psit"""
    for i in range(-num, 0):
        print(abs(i), end=" ")
        count += 1
        if count%7 == 0:
            print()
main(int(input()), 0)
