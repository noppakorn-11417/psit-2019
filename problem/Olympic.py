"""ez"""
def main():
    """EZ"""
    score_board = sorted([input().split() for _ in range(int(input()))])[::-1]
    score_board = sorted(score_board, key=lambda x: tuple(map(int, x[1:])))[::-1]
    rank, use_rank = [0], []
    for i in score_board:
        if i[1:] not in use_rank:
            rank += [max(rank)+rank.count(max(rank))]
        else:
            rank += [max(rank)]
        print(rank[-1], " ".join(i), sum(map(int, i[1:])))
        use_rank += [i[1:]]
main()
