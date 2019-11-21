"""psit"""
def main(num, seq, num2=1):
    """prime nnumber"""
    while num2 != 0:
        num2 = int(input())
        seq.append(num2)
    seq.sort()
    seq2 = [i for i in range(num+1)]
    for i in seq:
        seq2.remove(i)
    for i in seq2:
        print(i)
main(int(input()), list())
