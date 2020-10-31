"""
“大O记法”：对于单调的整数函数f，如果存在一个整数函数g和实常数c>0，使得对于充分大的n总有f(n)<=c*g(n)，
就说函数g是f的一个渐近函数（忽略常数），记为f(n)=O(g(n))。也就是说，在趋向无穷的极限意义下，
函数f的增长速度受到函数g的约束，亦即函数f与函数g的特征相似。
时间复杂度：假设存在函数g，使得算法A处理规模为n的问题示例所用时间为T(n)=O(g(n))，则称O(g(n))为算法A的渐近时间复杂度，
简称时间复杂度，记为T(n)
空间复杂度S(n):对一个算法在运行过程中临时占用存储空间大小的量度。
"""


def bubble_sort(li):
    """冒泡排序， 时间复杂度O(n)~O(n2), 稳定"""
    n = len(li)
    # 控制趟数
    for j in range(n - 1):
        count = 0
        # 进行一趟比较交换操作
        for i in range(n - 1 - j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                count += 1
        # 进行一趟比较后没有交换，说明列表已经有序
        if count == 0:
            break


def selection_sort(li):
    """选择排序，时间复杂度O(n2)~O(n2), 稳定"""
    n = len(li)
    # 控制趟数
    for j in range(n - 1):
        # 记录最小位置
        min_idx = j
        # 往后寻找最小值并进行交换
        for i in range(1+j, n):
            if li[i] < li[min_idx]:
                min_idx = i
        if min_idx != j:
            li[min_idx], li[j] = li[j], li[min_idx]


def insert_sort(li):
    """插入排序，时间复杂度O(n)~O(n2), 稳定"""
    n = len(li)
    for j in range(1, n):
        for i in range(j, 0, -1):
            # 与前面值比较若比前面值小，则进行交换
            if li[i] < li[i-1]:
                li[i-1], li[i] = li[i], li[i-1]
            else:
                break


def shell_sort(li):
    """希尔排序, 时间复杂度O(n1.3)~O(n2), 不稳定"""
    n = len(li)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            while i - gap >= 0:
                if li[i] < li[i-gap]:
                    li[i], li[i-gap] = li[i-gap], li[i]
                    i -= gap
                else:
                    break
        gap = gap // 2


def quick_sort(li, start, end):
    """快速排序, 时间复杂度O(nlogn)~O(n2), 不稳定"""

    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = li[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while li[high] >= mid and low < high:
            high -= 1
        li[low] = li[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while li[low] < mid and low < high:
            low += 1
        li[high] = li[low]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    li[low] = mid
    quick_sort(li, start, low-1)
    quick_sort(li, low+1, end)


def merge_sort(li):
    """归并排序, 时间复杂度O(nlogn)~O(nlogn),稳定"""
    if len(li) <= 1:
        return li
    # 二分分解
    mid = len(li) // 2
    left_list = merge_sort(li[:mid])
    right_list = merge_sort(li[mid:])
    # left与right的下标指针
    l, r = 0, 0
    res = []
    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            res.append(left_list[l])
            l += 1
        else:
            res.append(right_list[r])
            r += 1
    res = res + left_list[l:] + right_list[r:]
    return res


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(li, 0, len(li) - 1)
# li = merge_sort(li)
print(li)
