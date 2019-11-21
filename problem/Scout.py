"""EZ"""
def egg_pack(value):
    """EZ"""
    for _ in range(value):
        egg_limit, egg_weight = map(int, input().split()[1:])
        egg_cal(sorted((map(int, input().split()))), egg_limit, egg_weight)
 
def egg_cal(egg_data, limit, limit_weight):
    """EZ"""
    egg_cook, weight = [], 0
    while 1:
        if egg_data:
            egg = egg_data.pop(0)
            if len(egg_cook)+1 <= limit and weight+egg <= limit_weight:
                egg_cook += [egg]
                weight += egg
            else:
                break
        else:
            break
    print(len(egg_cook))
egg_pack(int(input()))
