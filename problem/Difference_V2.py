"""EZ"""
import json
def diff(list1, list2):
    """555"""
    union = list1+list2
    for i in set(list1).intersection(set(list2)):
        if list1.count(i) != list2.count(i):
            for _ in range(min(list1.count(i), list2.count(i))*2):
                union.remove(i)
        else:
            while i in union:
                union.remove(i)
    if not union:
        return print("ONAJI DAYO!")
    _ = [print(i, union.count(i)) for i in sorted(set(union))]
diff(json.loads(input()), json.loads(input()))
