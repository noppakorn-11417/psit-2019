"""pair"""
def main(avg, wg1, wg2, wg3):
    """Trunkskung"""
    wg4 = (avg*4)-wg1-wg2-wg3
    print("Overweight" if avg*4 >= 15000 else "Unbalance" if abs(wg1-avg) >= avg/2 or abs(wg2-avg)\
     >= avg/2 or abs(wg3-avg) >= avg/2 or abs(wg4-avg) >= avg/2 else "Pass %.2f"%wg4)
main(float(input()), float(input()), float(input()), float(input()))
