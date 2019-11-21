"""elo"""
def main(score_a, score_b, player):
    """elo"""
    elo_a = 1/(1+10**((score_b-score_a)/400))
    elo_b = 1/(1+10**((score_a-score_b)/400))
    if player == "A":
        return elo_a
    return elo_b
print("%.2f"%main(int(input()), int(input()), input()))
