class Clazz:
    def __init__(self, grade, place):
        self._name = "zhangsan!"
        self.grade = grade
        self.place = place

    @staticmethod
    def _lock():
        print("the class has been locked!")

    def say(self):
        Clazz._lock()
        print("asdfasdfasd")



if __name__ == '__main__':
    clazz = Clazz(3, "2 lou")
    clazz.say()
    print(clazz._name)

    print(issubclass(Clazz, object))