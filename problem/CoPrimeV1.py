"""psit"""
def gdc(number, temp=0):
    """fc inw nut"""
    num_max, num_min = max(number[0], number[1]), min(number[0], number[1])
    while num_min > 0:
        temp = num_min
        num_min = num_max%num_min
        num_max = temp
    return num_max
def co_prime(num1, num2):
    """co_prime"""
    co_gdc = gdc((num1, num2))
    if co_gdc == 1:
        return print("YES"), print(co_gdc)
    return print("NO"), print(co_gdc)
co_prime(int(input()), int(input()))
