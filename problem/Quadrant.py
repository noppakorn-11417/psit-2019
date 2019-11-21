"""EZXEX"""
def quadrant(point_x, point_y):
    """EZX"""
    if point_x > 0 and point_y > 0:
        return "Q1"
    elif point_x < 0 and point_y > 0:
        return "Q2"
    elif point_x < 0 and point_y < 0:
        return "Q3"
    elif point_x > 0 and point_y < 0:
        return "Q4"
    elif point_x == 0 and point_y != 0:
        return "Y"
    elif point_y == 0 and point_x != 0:
        return "X"
    else:
        return "O"
print(quadrant(int(input()), int(input())))
