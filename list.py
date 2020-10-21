def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2
    如果第一个和最后一个相同时则返回正确
    >>> same_first_last([3,4,2,8,3])
    True
    >>> same_first_last(['apple','banana','pear'])
    >>> same_first_last([4.0,4.5])
    """
    if len(L) >= 2 :
        if L[0] == L[-1] :
            return True
        else:
            return False

def is_longer(L1: list,L2: list) -> bool:
    """当且仅当L1长度大于L2长度时，返回True
    >>> is_longer([1,2,3],[4,5])
    True
    >>> is_longer(['abcdef'],['ab','cd','ef'])
    >>> is_longer(['a','b','c'],[1,2,3])
    """
    if len(L1) > len(L2) :
        return True
    else:
        return False


if __name__ == '__main__' :
    print(same_first_last([3,4,2,8,3]))
    print(same_first_last(['apple','banana','pear']))
    print(same_first_last([4.0,4.5]))

    print(is_longer([1,2,3],[4,5]))
    print(is_longer(['abcdef'],['ab','cd','ef']))
    print(is_longer(['a','b','c'],[1,2,3]))