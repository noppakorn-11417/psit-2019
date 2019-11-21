"""psit week3"""
def main(num):
    """i love psit"""
    for j in range(-num+1, num+1):
        for i in range(1, num-abs(j)+1):
            print(i, end=" ")
        print()
main(int(input()),)
