"""psit"""
import math as m
def catalan(num):
    """fibo"""
    return m.factorial((2*num))/(m.factorial((1+num))*m.factorial((num)))
print(int(catalan(int(input()))))
