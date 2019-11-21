"""psit"""
def gdc(number, temp=0):
    """fc inw nut"""
    num_max, num_min = max(number[0], number[1]), min(number[0], number[1])
    while num_min > 0:
        temp = num_min
        num_min = num_max%num_min
        num_max = temp
    return num_max
def main():
    """ez"""
    number_list = sorted([int(input()) for _ in range(int(input()))])
    while len(number_list) >= 2:
        cal = gdc((number_list.pop(0), number_list.pop(0)))
        number_list = [cal] + number_list
    print(number_list[0])
main()
