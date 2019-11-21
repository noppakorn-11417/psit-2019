"""psit week3"""
def main(num):
    """i love psit"""
    for j in range(-num+1, 1):
        print(" "*3*abs(j), end="")
        for i in range(1, num-abs(j)+1):
            print("%02d"%i, end=" ")
        print()
main(int(input()),)
