def change(x: int) -> str:
    """十进制转为二进制，12->1100"""
    s = ""
    while x > 0:
        b = x % 2
        s = str(b) + s
        x = x // 2
    return s



if __name__ == '__main__':
    print(change(12))
    print(change(11))
    