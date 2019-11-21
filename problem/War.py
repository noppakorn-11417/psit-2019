"""test"""
import json
def main(attack, deffend, ans=0):
    """ez"""
    defpin, att_pin, limit = 0, 0, len(deffend)
    while defpin != limit:
        if attack[att_pin] > deffend[defpin]:
            ans += attack[att_pin]
            att_pin += 1
        defpin += 1
    print(ans)
main(sorted(json.loads(input()), reverse=1), sorted(json.loads(input()), reverse=1))
