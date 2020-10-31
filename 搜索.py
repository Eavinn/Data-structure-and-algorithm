def binary_search(li, item):
    """二分查找,时间复杂度O(1)~O(nlogn)"""
    if not len(li):
        return False
    mid = len(li) // 2
    if li[mid] == item:
        return True
    elif item < li[mid]:
        return binary_search(li[:mid], item)
    else:
        return binary_search(li[mid+1:], item)


li = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(li, 3))
print(binary_search(li, 13))