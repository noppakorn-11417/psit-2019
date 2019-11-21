"""cat_walk"""
def main(step, stair_floor, stair_size=0, stair_distance=0, count=0):
    """cat walk"""
    for _ in range(stair_floor):
        stair_size = int(input())
        if step < stair_size:
            return print("NO")
        elif stair_distance >= stair_size:
            stair_distance -= stair_size
        else:
            count += 1
            stair_distance = step-stair_size
    print(count)
main(int(input()), int(input()))
