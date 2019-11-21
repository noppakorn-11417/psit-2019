"""EZ"""
def test_pack():
    """EZ"""
    for _ in range(int(input())):
        book_worm(int(input()), int(input()))
def book_worm(times, values):
    """EZ"""
    book_time = sorted([int(input()) for _ in range(values)])
    if book_time:
        while times >= book_time[0]:
            if book_time:
                times -= book_time.pop(0)
            if not book_time:
                break
    print(values-len(book_time))
test_pack()
