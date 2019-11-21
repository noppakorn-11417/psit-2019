"""ped"""
def main(range_ped):
    """ped.optimize"""
    ped = [int(input()) for _ in range(range_ped)]
    ped_k = int(input())
    ped_eq = ped.count(ped_k/2)
    peds = [ped.count(i)*ped.count(ped_k-i) for i in set(ped) if i < ped_k/2]
    print(int(sum(peds)+ped_eq*(ped_eq-1)*0.5))
main(int(input()))
