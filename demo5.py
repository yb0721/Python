#二分搜索
from typing import Any

def binary_search(L: list, v: Any) -> int:
    """返回L中value第一次出现的索引，如果value不在L中，则返回-1
    >>>binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
     0
    >>>binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
     2
    >>>binary_search([1, 3, 4, 4, 5, 7, 9, 10], 5)
     4
    >>>binary_search([1, 3, 4, 4, 5, 7, 9, 10], 10)
     7
    >>>binary_search([1, 3, 4, 4, 5, 7, 9, 10], -3)
     -1
    >>>binary_search([], -3)
     -1
    >>>binary_search([1], 1)
     0
    """

    #标记未知部分左侧和右侧的索引
    i = 0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0 <= i <len(L) and L[i] == v:
        return i
    else:
        return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod() 