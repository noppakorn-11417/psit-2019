"""ped"""
def main(deep, width):
    """ped"""
    daimond_sum = [0 for _ in range(width)]
    daimond = [list(map(int, input().split())) for _ in range(deep)]
    for k in daimond:
        for i, value in enumerate(k):
            daimond_sum[i] += value
    print(max(daimond_sum))
main(int(input()), int(input()))
