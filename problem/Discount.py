"""main"""
def book_event(buy):
    """EZ"""
    book_chart = []
    while buy != "ENTER":
        book_chart.append(int(buy))
        buy = input()
    book_chart = discount(book_chart)
    print(sum(book_chart))
def discount(book_chart):
    """EZ"""
    book, promo = len(book_chart), 0
    if 12 > book >= 6:
        promo = 1
    elif 20 > book > 11:
        promo = 2
    elif 25 > book >= 20:
        promo = 4
    elif book >= 25:
        promo = 4+((book-20)//5)
    return sorted(book_chart)[promo:]
book_event(input())
