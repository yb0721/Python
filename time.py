import datetime

def times(h: int, m: int ) -> int :
    """计算时针与分针的夹角
       判断分针与时针的前后，之后再进行计算
       b为时针现在的角度
       c为分针的角度
    """

    if h > 12:
        h = today.hour - 12
        b = 30 * (h + m / 60 )
        if b > 180:
            b = 360 - b
        else:
            b = b
        c = 6 * m
        if c > 180:
            c = 360 - c
        else:
            c = c
        s = b - c
        if s > 180:
            s = 360 - s
            return abs(s),b,c
        else:
            return abs(s),b,c
    else:
        b = 30 * (h + m / 60 )
        c = 6 * m
        s = b - c
        if s > 180:
            s = 360 - s
            return abs(s),b,c
        else:
            return abs(s),b,c

        

if __name__ == '__main__':
    today = datetime.datetime.today()
    print(times(today.hour, today.minute))
    print(times(1,20))
    # print(time(9,0))
    # print(time(3,0))
    # print(time(7,30))
    # print(time(6,0))