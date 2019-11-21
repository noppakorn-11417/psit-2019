"""hamburger"""
def main(num2):
    """despacito"""
    ans1 = ans2 = ans3 = ans4 = ans5 = ""
    for i in num2:
        text1 = "  *  "*(i == "U")+"  *  "*(i == "D")+"  *  "*(i in "LR")
        text2 = " *** "*(i == "U")+"  *  "*(i == "D")+" *   "*(i in "L")+"   * "*(i in "R")
        text3 = "* * *"*(i == "U")+"* * *"*(i == "D")+"*****"*(i in "LR")
        text4 = "  *  "*(i == "U")+" *** "*(i == "D")+" *   "*(i in "L")+"   * "*(i in "R")
        text5 = "  *  "*(i == "U")+"  *  "*(i == "D")+"  *  "*(i in "LR")
        ans1, ans2, ans3, ans4, ans5 = ans1+text1+" ", \
        ans2+text2+" ", ans3+text3+" ", ans4+text4+" ", ans5+text5+" "
    return print(ans1), print(ans2), print(ans3), print(ans4), print(ans5)
main(input())
