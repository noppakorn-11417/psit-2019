"""pair"""
def mlist(count, chik):
    """food"""
    return mlist(count+1, chik+[float(input())]) if count <= 24\
     else print(len(list(filter(lambda x: abs(x-60) <= 10, chik))))
mlist(1, [])
