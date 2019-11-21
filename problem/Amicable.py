"""love psit"""
import math
def fast_factor(num):
    """optimize amicalble"""
    if num == 0:
        return -1
    if num%10 in {1, 7, 9}:
        return 0
    if num%2 == 0:
        return sum([i+num//i for i in range(2, int(math.sqrt(num))+1) if num%i == 0])+1
    if num%2 != 0:
        return sum([i+num//i for i in range(3, int(math.sqrt(num))+1, 2) if num%i == 0])+1
def amicable_num(number):
    """optimize amicable"""
    sum_amicable = set()
    memo = set()
    for pair1 in range(220, number+1):
        if pair1 in memo:
            continue
        pair2 = fast_factor(pair1)
        if fast_factor(pair2) == pair1 and pair2 != pair1:
            sum_amicable.add(pair1+pair2)
        memo.add(pair2)
    print(sum(sum_amicable))
amicable_num(int(input()))
