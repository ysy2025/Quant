def method(self):
    return 1

klass = type('MyClass', (object, ), {'method':'method'})

if __name__ == '__main__':
    instance = klass()
    print(instance)