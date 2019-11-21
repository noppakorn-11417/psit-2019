"""EZ"""
def gas(want, limit, amount, count=0, distance=0):
    """ez"""
    station = [0]+[int(input()) for i in range(amount)]
    station_point = sorted([0]+[station[i+1]-station[i] for i in range(amount-1)])
    if station_point[0] >= limit or station_point[-1] > limit:
        return print("depleted")
    while distance+limit < want:
        if distance + limit not in station:
            count += 1
            distance = max([i for i in station if i < distance + limit])
        elif distance + limit in station:
            distance += limit
            count += 1
    print(count)
gas(float(input()), float(input()), int(input()))
