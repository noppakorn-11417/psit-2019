"""psit"""
def blackjack(hand):
    """evil doctor"""
    ans = 0
    count = 0
    for _ in range(hand):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            ans += 10
        elif card == "A":
            ans += 1
            count += 1
        else:
            ans += int(card)
    if count > 0 and ans+10 <= 21:
        ans += 10
    print(ans)
blackjack(int(input()))
