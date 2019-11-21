"""psit"""
def main(num):
    """fibo"""
    if num == 0:
        return print(0)
    calp, calm = (1+(5**0.5))/2, (1-(5**0.5))/2
    print(round(((calp**num)+(calm**num))/5**0.5))
main(int(input()))
