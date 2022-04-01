import types
import unittest

"""
这里的TestAccess 是 TestCase 的子类,定义了一些希望类可以通过的测试
实际被测试的对象被忽略了
它通过self.object被引用,但是没有提供定义,使得TestCase子类保持抽象
"""
class TestAccss(unittest.TestCase):
    def test_should_add_and_get_attribute(self):
        self.object.new_attribute = True
        self.assertTrue(self.object.new_attribute)
    def test_shold_fail_on_missing(self):
        self.assertRaises(AttributeError, lambda : self.object.undefined)

class SomeClass:
    pass

class Test_EmptyClass(TestAccss):
    def setUp(self):
        self.object = SomeClass()

class Test_NameSpace(TestAccss):
    def setUp(self):
        self.object = types.SimpleNamespace()

class Test_Object(TestAccss):
    def setUp(self):
        self.object=object()

def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Test_EmptyClass))
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Test_NameSpace))
    s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Test_Object))
    return s

if __name__ == '__main__':
    t = unittest.TextTestRunner()
    t.run(suite())