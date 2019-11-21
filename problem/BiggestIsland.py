"""psit"""
import json
def flatten(string_list):
    """flatten"""
    return json.loads("["+"".join([str(i) for i in string_list if i not in "[]"])+"]")
 
def discover(island_area, log_horizon, row, col, mark=1):
    """EZ"""
    max_row, max_col = len(island_area), len(island_area[0])
    if log_horizon[row][col] >= 1:
        return 0
    if island_area[row][col]:
        log_horizon[row][col] = mark
        for i in range(max(0, row-1), min(max_row, row+2)):
            for j in range(max(0, col-1), min(max_col, col+2)):
                discover(island_area, log_horizon, i, j, mark)
        return 1
    return 0
 
def francis_drake():
    """volyager of storm"""
    high, width = map(int, input().split())
    island_area = [list(map(int, input().split())) for _ in range(high)]
    log_horizon = [[0 for _ in range(width)] for _ in range(high)]
    marker_gen = (i+2 for i in range(2501))
    marker = next(marker_gen)
    for row in range(high):
        for col in range(width):
            if discover(island_area, log_horizon, row, col, marker):
                marker = next(marker_gen)
    log_horizon = flatten(str(log_horizon))
    print(max([log_horizon.count(i+2) for i in range(marker+1)]))
 
francis_drake()
