"""psit"""
def main(count, finish):
    """i love psit"""
    for _ in range(abs(count-finish)+1):
        if finish < count:
            print(count)
            count -= 1
        else:
            print(count)
            count += 1
main(int(input()), int(input()))
