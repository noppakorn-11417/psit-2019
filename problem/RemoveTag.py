"""psit"""
def main(htmltext, status=0):
    """fibo"""
    ans = []
    for i in htmltext:
        if i == "<":
            status = 1
        elif i == ">":
            status = 0
            ans.append(i)
        elif status == 0:
            ans.append(i)
    print((" ".join("".join(ans).split(">")).split()))
main(input())
