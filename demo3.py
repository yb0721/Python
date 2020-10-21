#使用嵌套for循环，打印直角三角形
for i in range(1,8):
    print(i*'T')#非嵌套方法
for i in range(7):
    for j in range(i+1):
        print('T',end="")
    print()#嵌套方法

#使用嵌套for循环，打印直角三角形，斜边相反
for i in range(2,9):
    for j in range(0,8-i):
        print(" ",end="")
    for c in range(i-1):
        print("T",end="")
    print()
    