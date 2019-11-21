""" i sleep"""
def main(ball, count=0):
    """ball deng deng"""
    while ball >= 0.01:
        ball *= 0.6
        count += ball >= 0.01
    print(count)
main(float(input()))
