"""pair programing"""
def main(score):
    """grade fillter"""
    print("ERR" if score >= 100 or score < 0 else "A" if score >= 95 else "B+" if score >= 90 \
    else "B" if score >= 85 else "C+" if score >= 80 else "C" if score >= 75 \
     else "D+" if score >= 70 else "D" if score >= 65 else "F+" if score >= 60 else "F")
main(float(input()))
