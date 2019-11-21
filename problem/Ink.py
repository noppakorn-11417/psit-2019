"""EZ"""
from math import hypot, ceil
def ink():
    """EZ"""
    speed, report = input().split()
    report_data = [list(map(int, input().split())) for _ in range(int(report))]
    for home_x, home_y in report_data:
        print(ceil((3.1416*(hypot(home_x, home_y)**2))/int(speed)))
ink()
