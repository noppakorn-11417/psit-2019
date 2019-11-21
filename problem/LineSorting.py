"""psit"""
def main(num):
    """fibo"""
    print(*sorted([input() for _ in range(num)], key=len), sep="\n")
main(int(input()))
