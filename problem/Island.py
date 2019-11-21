"""EZ"""
def discover(island_area, log_horizon, row, col):
    """EZ"""
    max_row, max_col = len(island_area), len(island_area[0])
    if log_horizon[row][col] == 1:
        return 0
    else:
        log_horizon[row][col] = 1
        if island_area[row][col]:
            for i in range(max(0, row-1), min(max_row, row+2)):
                for j in range(max(0, col-1), min(max_col, col+2)):
                    discover(island_area, log_horizon, i, j)
            return 1
        else:
            return 0
def columbus(count=0):
    """EZ"""
    high, width = map(int, input().split())
    island_area = [list(map(int, input().split())) for _ in range(high)]
    log_horizon = [[0 for _ in range(width)] for _ in range(high)]
    for row in range(high):
        for col in range(width):
            count += discover(island_area, log_horizon, row, col)
    print(count)
columbus()
