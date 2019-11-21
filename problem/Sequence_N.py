"""n"""
def main(size):
    """k"""
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size-1:
                print("*", end="")
            elif i == j or j == size:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))
