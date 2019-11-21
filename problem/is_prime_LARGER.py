"""ez"""
import random as r
def is_prime_x100(number):
    """ 0.25**100 error rate"""
    for _ in range(100):
        if not is_prime(number):
            return False
    return True
def is_prime(number):
    """rabin miler 3/4 prim test"""
    if number == 2:
        return True
    if number == 3:
        return True
    if number == 1:
        return False
    if number%2 == 0:
        return False
    return powermod(r.randrange(2, number-2), number-1, number) == 1
 
def powermod(random_num, power_num, modular_num):
    """test"""
    if power_num == 0:
        return 0
    cal = pow(random_num, power_num, modular_num)
    cal2 = pow(cal, power_num, modular_num)
    if cal2 == 1 and cal2 != 1 and cal2 != modular_num-1:
        return 0
    return cal
print(is_prime_x100(int(input())))
