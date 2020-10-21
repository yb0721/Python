#函数add（a,b）测试
def add(a: int ,b: int) -> int:
    if a > 0 and b > 0:
        return a + b
    else:
        return -a-b

if __name__ == '__main__':
    print(add(-6, 0))