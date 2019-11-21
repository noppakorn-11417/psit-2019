"""Sequence XI"""
import json
def main(jsonn, score):
    """ box """
    x_x = []
    for i in sorted(jsonn.keys()):
        if float(jsonn[i]) >= score:
            x_x.append("%s\t%.2f"%(i, jsonn[i]))
    if len(x_x) != 0:
        print(*x_x, sep="\n")
    else:
        print("Nope")
main(json.loads(input()), float(input()))
