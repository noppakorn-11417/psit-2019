"""EZ"""
def diff():
    """555"""
    floor = [i for i in range(1, int(input())+1)]
 
    now_floor = floor[int(input())-1]
    command = input()
    while command != "END":
        if command == "DOWN":
            now_floor = floor[max(0, now_floor-2)]
        else:
            now_floor = floor[min(now_floor, floor[-1]-1)]
        command = input()
    print(now_floor)
diff()
