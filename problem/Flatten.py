"""psit"""
import json
def main(string_list):
    """fc inw nut"""
    listed = [str(i) for i in string_list if i in "0123456789. ,-"]
    print(sorted(json.loads("["+"".join(listed)+"]"), key=float, reverse=True))
main(input())
