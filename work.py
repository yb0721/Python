def weeks_elapsed(day1: int,day2: int) -> int:
    """day1 and day2 are days in the same year.Return the number of full weeks
       that have elapsed 
       between the two days.
    >>> weeks_elpased(3,20)
    2
    >>> weeks_elpased(20,3)
    2
    """
    return abs(day2-day1) // 7

def square(x: int) -> int:
    """计算x的平方"""
    return x ** 2

if __name__ == '__main__':
    # print (weeks_elapsed(3,20))
    # print(weeks_elapsed(20,3))
    # print(weeks_elapsed(8,5))
    print(square(3))