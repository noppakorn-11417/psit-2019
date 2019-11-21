"""psit"""
def main(group1, group2):
    """fibo"""
    group = list({input() for i in range(group1)}.intersection({input() for i in range(group2)}))
    if group:
        return print(*sorted(group)[::-1], sep="\n")
    return print("Nope")
main(int(input()), int(input()))
