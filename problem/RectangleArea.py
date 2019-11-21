"""EZ"""
def main(data_a, data_b):
    """i sleep"""
    connerlow_a = [data_a[0], data_a[1]]
    connerlow_b = [data_b[0], data_b[1]]
    connerhigh_a = [connerlow_a[0]+data_a[2], connerlow_a[1]+data_a[3]]
    connerhigh_b = [connerlow_b[0]+data_b[2], connerlow_b[1]+data_b[3]]
    width = min(connerhigh_a[0], connerhigh_b[0])-max(connerlow_a[0], connerlow_b[0])
    high = min(connerhigh_a[1], connerhigh_b[1])-max(connerlow_a[1], connerlow_b[1])
    area = width*high
 
    if area > 0:
        print(area)
    else:
        print("no overlapping")
 
main(list(map(int, input().split())), list(map(int, input().split())))
