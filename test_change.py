import unittest
import change

class TestChange(unittest.TestCase):
    """测试十进制转换为二进制"""

    def test_even_number(self):
        """测试偶数"""

        expected = '1100'
        result = change.change(12)
        self.assertEqual(expected,result)

unittest.main()