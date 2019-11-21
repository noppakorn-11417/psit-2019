"""kayukkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"""
def main(num, weight):
    """shippppppppppppp"""
    ship = sorted(list(map(int, weight)))
    num = 0
    while len(ship) > 2:
        pair = sorted([[ship[i], ship[i+1]] for i in range(len(ship)-1)], key=lambda x: x[1]-x[0])
        num += abs(pair[0][0]-pair[0][1])
        ship.remove(pair[0][0])
        ship.remove(pair[0][1])
    print(num)
main(input(), input().split())
