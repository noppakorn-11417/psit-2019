"""psit"""
def main(number, temp=0):
    """fc inw nut"""
    num_max, num_min = max(number[0], number[1]), min(number[0], number[1])
    while num_min > 0:
        temp = num_min
        num_min = num_max%num_min
        num_max = temp
    print(num_max)
main((int(input()), int(input())))
