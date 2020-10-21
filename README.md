Python数据类型总结：
   字符串（str），整型（int），列表（list），元组（tuple），字典（dirt），浮点型（float）
   布尔型（boolean）

测试数据类型：type()

布尔型：只有两个值，分别为True 和 False，用作条件判断

各数据类型添加元素：
   字符串：a = 'app'
                a + 'x'
                a = 'appx'
   列表：a = [1,2]
             a.append(3)
             a = [1,2,3]
   元组：不能添加，只能创建，不能添加
   字典：keys不能为列表，字典类型，查看keys：d.keys(),查看values：d.values()
             d = {'a': 1, 'b': 2}
             d['c'] = 3
             d = {'a': 1, 'b': 2, 'c': 3}

各数据类型的删除元素：
 ***凡是要先删除的话，必先搜索（即定位到索引）到要删除的元素位置
  字符串：不能删除
  列表：a = [1,2]
            del a[0]
            a = [2]
   元组：不能删除，只能创建
   字典：d = {'a': 1, 'b': 2}
             d.pop('a')
             d = {'b': 2}

各数据类型搜索元素：
   字符串：a = 'apple'
                a[-2]
                'l'
   除字典外方法都和字符串相同
   字典：通过key搜索到对应的value值 ***不能通过value找到对应的key值
             d = {'a': 1, 'c': 3, 'b': 2}
             d['c']
             3

各数据类型更改元素：
   列表：a = [1, 2, 3]
             a[0] = 2
             a = [2, 2, 3]
   字典：a = {'b': 1, 'c': 2}
             a['b'] = 6
             a = {'b': 6, 'c': 2}

各数据类型的排序：
****sorted函数:所有数据类型可用
      sort方法：仅list数据类型可用
   列表：d = [1, 2, 5, 3, 8, 9]
             d.sort()
             d = [1, 2, 3, 5, 8, 9]
   元组：d = (1, 2, 6, 5, 3,)
             sorted(d)
             d = [1, 2, 3, 5, 6]
             d = tuple(d)
             d = (1, 2, 6, 5, 3)
   字典：d = {'a': 2, 'A': 1, 'c': 3, 'b': 2}
             sorted(d)
             d = ['A', 'a', 'b', 'c']

各数据类型的相互转换：
     列表转元组：tuple(转换对象)
     元组转列表：list(转换对象)
     其他相同

查看各数据类型元素长度：len()
   字符串：a = 'abc'
                 len(a)
                 3
   列表：a = [1, 2, 3]
             len(a)
             3
   字典：a = {'b': 1, 'c': 2}
             len(a)
             2
   元组：a = （1,2,）
             len(a)
             2

if的使用：
               if 条件：
                    结果
   eg：a = 18
           if a>17:
               print(2)
           2
    if条件：
        结果
    elif条件：
        结果
注： 可省略if条件,只能用于bool型
      eg：if puzzle == view:     ==   return puzzle == view
                 return Ture
注：条件连接用and，满足一个条件用or，break用于跳出条件语句，continue用于继续执行条件语句

for in 的使用：for x in range(1, 10):
                           print(x)

while 语句的使用：count = 0
                              while (count < 9):
                                  print 'The count is:', count
                                  count = count + 1


函数的表达方式：def 函数名(参数：数据类型) -> 数据类型：
                           if __name__ == '__main__':

若变量名字太长可在函数前写出代替的名字

单元测试：
   导入测试框架：import unittest
                          unittest.main()

线性搜索：一步一步搜索
二分搜索：先一分为而将不正确的一半删除，再进行搜索
比较：二分搜索更方便，效率更高

方法的使用
     1. strip()方法：删除开头或结尾的指定字符
         a = '000123000'
         a.strip('0')
         a = '123'
     2. lstrip()方法：删除左边的指定字符
         a = '000123000'
         a.lstrip('0')
         a = '123000'
     3.replace()方法：将旧的字符串替换成新的字符串str.replace(旧的字符串，新的字符串，替换次数)
         a = '3.14159'
         a.replace('.', '', 1)
         a = '314159'
     4.isnumeric()方法：检测字符串是否由数字组成，返回值为bool型
         a = '3.14159'        b = '123'
         a.isnumeric()         b.isnumeric()
         False                     True
     5.isinstance(1，int)方法：判断所要检测对象的数据类型
         a = 2
         isinstance(a, int)
         True

函数：
enumerate()函数的使用:
	 d = [['ab2'], ['-123'], ['False', '3.2']]
>>> for i in d:
...     for j, x in enumerate(i):
...         print(j, x)
...
0 ab2
0 -123
0 False
1 3.2
format()函数的使用：
	>>> a = 25 / 31
	>>> a
	0.8064516129032258
	>>> format(a, '.0%')
	'81%'s
	>>> format(a, '.2%')
	'80.65%'
注：'.0%'中的0为转换为百分数后可以保留的小数点位数

类型转换：
都可以强转，但bool类型不能强转
int强转：int()
Str强转：str()
float强转：float()
字符串转bool：x =True(只能重新赋值，不能强转)

判断字符串中是否含有某个数值： 
 >>> x = 'abc'
>>> 'b' in x
True

列表中的列表元素相加：
	    x = [[2, 4, 5], [3, 1, 4, 5]]
	 a = 0
	>>> for i in x:
	...     a = a + i[2]
	... print(a)
	9