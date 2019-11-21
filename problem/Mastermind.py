"""cat_walk"""
def main(code, guess, new_code, new_guess):
    """cat walk"""
    black, white, blank = 0, 0, 4
    for i, j in zip(code, guess):
        if i == j:
            black += 1
            continue
        new_code += i
        new_guess += j
    for i in new_guess:
        if i in new_code:
            white += 1
            new_code[new_code.index(i)] = "x"
    blank -= black+white
    print("B"*black+"W"*white+"O"*blank)
main(list(input()), list(input()), [], [])
