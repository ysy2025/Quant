class Unit:
    factor = 1.0
    standard = None
    name = ""

    @classmethod
    def value(class_, value):
        if value is None: return None
        return value/class_.factor

    def convert(class_, value):
        if value is None: return None
        return value ( class_.factor)



if __name__ == '__main__':
    pass