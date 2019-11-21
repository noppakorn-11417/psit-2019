"""psit"""
def main(count):
    """i love psit"""
    result = 0
    for _ in range(count):
        result += grade(float(input()))
    result = int((result/count)*100)
    print("%.2f"%(result/100))
def grade(score):
    """i sleep"""
    if score >= 95:
        score = 4
    elif score >= 90:
        score = 3.5
    elif score >= 85:
        score = 3
    elif score >= 80:
        score = 2.5
    elif score >= 75:
        score = 2
    elif score >= 70:
        score = 1.5
    elif score >= 65:
        score = 1
    elif score >= 60:
        score = 0.5
    else:
        score = 0
    return score
main(int(input()))
