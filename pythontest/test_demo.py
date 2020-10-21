import unittest

import demo

from HTMLTestRunner import HTMLTestRunner

class TestDemo(unittest.TestCase):
    def testAdd_01(self):
        """测试a>0 and b>0"""
        expected = 5
        result = demo.add(2, 3)
        self.assertEqual(expected, result)

    def testAdd_02(self):
        """测试a=0 and b=0"""
        expected = 0
        result = demo.add(0, 0)
        self.assertEqual(expected, result)

    def testAdd_03(self):
        """测试a=0 and b<0"""

        expected = 3
        result = demo.add(0, -3)
        self.assertEqual(expected, result)

    def testAdd_04(self):
        """测试a=0 and b>0"""

        expected = -3
        result = demo.add(0, 3)
        self.assertEqual(expected, result)

    def testAdd_05(self):
        """测试a>0 and b=0"""

        expected = -6
        result = demo.add(6, 0)
        self.assertEqual(expected, result)

    def testAdd_06(self):
        """测试a<0 and b=0"""

        expected = 6
        result = demo.add(-6, 0)
        self.assertEqual(expected, result)

    def testAdd_07(self):
        """测试a=0 and b>0"""

        expected = -2
        result = demo.add(-1, 3)
        self.assertEqual(expected, result)

    def testAdd_08(self):
        """测试a<0 and b<0"""

        expected = 4
        result = demo.add(-1, -3)
        self.assertEqual(expected, result)

    def testAdd_09(self):
        """测试a>0 and b<0"""

        expected = 2
        result = demo.add(1, -3)
        self.assertEqual(expected, result)


    

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(TestDemo("testAdd_01"))
    suite.addTest(TestDemo("testAdd_02"))
    suite.addTest(TestDemo("testAdd_03"))
    suite.addTest(TestDemo("testAdd_04"))
    suite.addTest(TestDemo("testAdd_05"))
    suite.addTest(TestDemo("testAdd_06"))
    suite.addTest(TestDemo("testAdd_07"))
    suite.addTest(TestDemo("testAdd_08"))
    suite.addTest(TestDemo("testAdd_09"))

    f = "G:\\test1.html"
    fp = open(f, "wb")
    runner = HTMLTestRunner(stream=fp, title="测试结果", description="测试用例执行情况")
    runner.run(suite)
    fp.close()

unittest.main()