"""despacito"""
def main(text1, boxa=1, boxb=0, boxc=0):
    """sheep hide"""
    for i in text1:
        if i == "A":
            boxa, boxb, boxc = boxb, boxa, boxc
        if i == "B":
            boxa, boxb, boxc = boxa, boxc, boxb
        if i == "C":
            boxa, boxb, boxc = boxc, boxb, boxa
    print("1"*(boxa == 1)+"2"*(boxb == 1)+"3"*(boxc == 1))
main(input())
