"""psit week3"""
def main(num, count, seq):
    """i love psit"""
    count = (num-1)*2
    for j in range(-num+1, 1):
        print(" "*3*abs(j), end="")
        for i in range(1, (num*2)-count):
            if i > ((num*2-count)//2):
                seq -= 1
            else:
                seq += 1
            print("%02d"%seq, end=" ")
        print()
        seq = 0
        count -= 2
    for j in range(1, num+1):
        print(" "*3*abs(j), end="")
        for i in range(1, (num*2)+count):
            if i > ((num*2+count)//2):
                seq -= 1
            else:
                seq += 1
            print("%02d"%seq, end=" ")
        print()
        seq = 0
        count -= 2
main(int(input()), 0, 0)
