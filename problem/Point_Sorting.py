"""EZ"""
def point_sort(num):
    """sort"""
    point = sorted([input().split() for _ in range(num)], key=lambda x: int(x[1]))[::-1]
    for i in sorted(point, key=lambda x: int(x[0])+int(x[1])):
        print("%s %s"%tuple(i))
def data_pack(num):
    """input pack"""
    for _ in range(num):
        point_sort(int(input()))
data_pack(int(input()))
