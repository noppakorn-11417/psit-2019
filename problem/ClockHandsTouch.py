"""psit"""
def main(hour, minn):
    """despacito"""
    cal = (((hour+(0.5*minn)/6))-minn)
    print(bool(cal < 6 and cal >= 0))
main(int(input())*30, int(input())*6)
