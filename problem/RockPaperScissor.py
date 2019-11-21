"""despacito"""
def mian(text_a, score_a=0, score_b=0):
    """despacito"""
    text_b = text_a[::-1]
    for i in range(0, len(text_a), 2):
        score_a += (text_a[i:i+2] in "RS SP PR")
        score_b += (text_b[i:i+2] in "RS SP PR")
    print("DRAW"*(score_a == score_b)+"A win"*(score_a > score_b)+"B win"*(score_a < score_b),\
     "%s%s"%(max(score_a, score_b), str(-min(score_a, score_b))*(score_a != score_b)))
mian(input())
