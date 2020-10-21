# 设计一个函数，对于身份证这个字符串
# 取出对应的性别：'男'、'女'
# 取出对应的生日：'20010723'
def sex(x: str) -> str:
    """取出身份证倒数第二位。判断性别"""
    z = int(x[-2])
    if z % 2 == 0:
        return "性别为女"
    else:
        return "性别为男"

def bir(x: str) -> str:
    """从身份证中取出生日"""
    a = x[6:10] +"年"
    b = x[10:12] +"月"
    c = x[12:14] + "日"
    return a+b+c

if __name__ == '__main__':
    print(sex('362421200107237450')) 
    print(bir('362421200107237640'))

    #用for in 制作九九乘法表
#1.小九九，直角三角形
for i in range(1,10):
    for j in range(1,i+1):
        if (j*i<10):
            print("%s*%s=%s"%(j,i,j*i)+"  ",end="")
        else:
            print("%s*%s=%s"%(j,i,j*i)+" ",end="")
    print()
#2.小九九，倒三角
for i in range(1,10):
    for j in range(i,10):
        print("%s*%s=%s"%(i,j,i*j)+" ",end="")
    print()
#3.大九九，长方形，带重复
for i in range(1,10):
    for j in range(1,10):
        print("%s*%s=%s"%(j,i,i*j)+" ",end="")
    print()

#对于DNA，A,T,C,G,U,实现A->T,U,C->G
#非函数
DNA = {'A': 'T,U','C': 'G'}
DNA['A']
DNA['C']

