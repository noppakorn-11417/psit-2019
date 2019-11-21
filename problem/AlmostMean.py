"""Sequence XI"""
def main(qty):
    """ box """
    id_s = []
    for _ in range(qty):
        id_s.append(input().split())
    id_s.sort(key=lambda x: float(x[1]))
    mean = sum([float(id_s[i][1]) for i in range(qty)])/qty
    new_list = [(id_s[i]) for i in range(qty) if float(id_s[i][1]) < mean]
    print("%s\t%s"%tuple(new_list[-1]))
main(int(input()))
