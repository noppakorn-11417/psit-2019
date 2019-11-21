"""pair"""
import heapq
def mlst(count, lst):
    """manual for loop to create lst"""
    return mlst(count+1, lst+[int(input())]) if count <= 8  else print(*heapq.nlargest(1, lst))
mlst(1, [])
