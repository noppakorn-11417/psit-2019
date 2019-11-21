"""fc inw bas"""
def main(text):
    """fc inw bas"""
    gram2 = [text[i:2+i] for i in range(len(text)-1)]
    max_gram = max([gram2.count(i) for i in set(gram2)])
    ans_list = [i for i in set(gram2)if max_gram == gram2.count(i)]
    gram2 = [i for i in gram2 if i in ans_list]
    print(gram2[0], max_gram, sep="\n")
main(input())
