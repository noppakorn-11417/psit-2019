"""EZ"""
def main(macaron):
    """i sleep"""
    sml = [0, 0, 0]
    while macaron >= 24:
        sml[-1] += macaron//min(24, macaron)
        macaron -= min(24, macaron)*(macaron//min(24, macaron))
    while 24 > macaron > 12:
        sml[-1] += macaron//min(24, macaron)
        macaron -= min(24, macaron)*(macaron//min(24, macaron))
    while 12 >= macaron > 6:
        sml[1] += macaron//min(12, macaron)
        macaron -= min(12, macaron)*(macaron//min(12, macaron))
    while 6 >= macaron > 0:
        sml[0] += macaron//min(6, macaron)
        macaron -= min(6, macaron)*(macaron//min(6, macaron))
    print(*sml, sep="\n")
main(int(input()))
