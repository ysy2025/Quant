import re

if __name__ == '__main__':
    pass
    a = r"zhangsan\asdfa/"

    r1 = re.compile("a")
    r1.findall(a)