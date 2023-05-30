class MyDesc:
    def __init__(self):
        self.name = "zhangsan"
        self.age = 18



if __name__ == '__main__':
    mydesc = MyDesc()
    print(mydesc.__dict__)