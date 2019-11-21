"""psit week3"""
def main(num, count):
    """i love psit"""
    for _ in range(1, num+1):
        for i in range(1+count, num+count+1):
            print(i, end=" ")
        count += num
        print()
main(int(input()), 0)
