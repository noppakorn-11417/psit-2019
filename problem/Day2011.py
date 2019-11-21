"""fc inw bas"""
def main(day, month):
    """fc inw bas"""
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday ", "Friday", "Saturday"]
    calendar = [(31, week[6:7]+week[0:6]), (28, week[2:7]+week[0:2]), (31, week[2:7]+week[0:2]),\
     (30, week[5:7]+week[0:5]), (31, week), (30, week[3:7]+week[0:3]), (31, week[5:7]+week[0:5]), \
     (31, week[1:]+week[0:1]), (30, week[4:]+week[0:4]), (31, week[6:7]+week[0:6]),\
     (30, week[2:7]+week[0:2]), (31, week[4:]+week[0:4])]
    ans = []
    for i in zip(list(range(1, calendar[month-1][0]+1)), calendar[month-1][1]*5):
        ans += [i[1]]
    print(ans[day-1])
main(int(input()), int(input()))
