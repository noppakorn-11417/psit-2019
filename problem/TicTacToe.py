"""EZ"""
def diff(tic):
    """555"""
    win1 = tic[0]
    win2 = tic[1]
    win3 = tic[2]
    win4 = tic[0][0]+tic[1][0]+tic[2][0]
    win5 = tic[0][1]+tic[1][1]+tic[2][1]
    win6 = tic[0][2]+tic[1][2]+tic[2][2]
    win7 = tic[0][0]+tic[1][1]+tic[2][2]
    win8 = tic[0][2]+tic[1][1]+tic[2][0]
    if len(set(win1)) < 2 and set(win1) != {"-"}:
        winner, status = win1[0], "WIN"
    elif len(set(win2)) < 2 and set(win2) != {"-"}:
        winner, status = win2[0], "WIN"
    elif len(set(win3)) < 2 and set(win3) != {"-"}:
        winner, status = win3[0], "WIN"
    elif len(set(win4)) < 2 and set(win4) != {"-"}:
        winner, status = win4[0], "WIN"
    elif len(set(win5)) < 2 and set(win5) != {"-"}:
        winner, status = win5[0], "WIN"
    elif len(set(win6)) < 2 and set(win6) != {"-"}:
        winner, status = win6[0], "WIN"
    elif len(set(win7)) < 2 and set(win7) != {"-"}:
        winner, status = win7[0], "WIN"
    elif len(set(win8)) < 2 and set(win8) != {"-"}:
        winner, status = win8[0], "WIN"
    else:
        return print("DRAW")
    print(winner, status)
diff([input() for _ in range(3)])
