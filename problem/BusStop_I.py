"""why bus station not sort"""
def bus(bus_size, station):
    """EZ"""
    people = sorted([tuple(map(int, input().split())) for _ in range(station)], key=lambda x: x[0])
    capacity, count = [], 0
    for i in range(station):
        if people[i][0] in capacity:
            capacity, count = deploy(capacity, people[i][0], count)
        if len(capacity) < bus_size:
            capacity += que(people[i], abs(len(capacity)-bus_size), station)
    print(count)
 
def que(station, limit, last_station):
    """EZ"""
    return [i for i in station[1:] if i >= station[0] and i <= last_station][:limit]
 
def deploy(listed, station, count):
    """EZ"""
    new_capacity = [i for i in listed if i != station]
    return new_capacity, abs(len(listed)-len(new_capacity))+count
 
bus(int(input()), int(input()))
