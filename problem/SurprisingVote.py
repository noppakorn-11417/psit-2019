"""psit"""
def main(score, hscore):
    """i love psit"""
    mscore = score-hscore if score-hscore < hscore else hscore
    lscore = score-hscore-mscore
    if abs(hscore-lscore) <= 2:
        print("Not surprising")
    else:
        print("Surprising")
main(float(input()), float(input()))
