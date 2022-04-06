"""
说明文档是很重要的
python 文档通常使用 ReStructured Text 标记来写
docstring 是必须的

docstrings在python中,可以通过以下3中方式使用
内部的help()函数
doctest工具可以在docstrings中查找示例,并且把它们当做测试用例运行
类似Sphinx和dpydoc这样的外部工具提取帮助文档

下面是一个案例,结合单元测试进行解析
"""

import unittest

def factorial(n):
    """Compute n! recursively!

    :param n: an integer >= 0
    :return: n!

    Because of Python's stack limitation, this won't
    compute a value larger than about 1000!

    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)

class TestDict(unittest.TestCase):
    def test_0(self):
        a = factorial(0)
        self.assertEqual(a, 1)
        self.assertTrue(isinstance(a, int))

    def test_1(self):
        a = factorial(1)
        self.assertEqual(a, 1)
        self.assertTrue(isinstance(a, int))

    def test_5(self):
        a = factorial(5)
        self.assertEqual(a, 120)
        self.assertTrue(isinstance(a, int))

if __name__ == '__main__':
    print(factorial(0))

    unittest.main()