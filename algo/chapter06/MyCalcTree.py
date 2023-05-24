def make_sum(a, b):
    return ("+", a, b)


def make_sub(a, b):
    return ("-", a, b)


def make_multi(a, b):
    return ("*", a, b)


def make_div(a, b):
    return ("/", a, b)


def is_basic_exp(a):
    # 判断是不是简单表达式;如果是tuple,则不是;如果不是tuple,则是
    return not isinstance(a, tuple)


def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    else:
        return make_sum(a, b)


def eval_sub(a, b):
    if is_number(a) and is_number(b):
        return a - b
    else:
        return make_sub(a, b)


def eval_multi(a, b):
    if is_number(a) and is_number(b):
        return a * b
    else:
        return make_multi(a, b)


def eval_div(a, b):
    if is_number(a) and is_number(b) and b!= 0:
        return a / b
    if a == 0 and b != 0:
        return 0
    if is_number(a) and is_number(b) and b == 0:
        raise ZeroDivisionError
    else:
        return make_div(a, b)

def eval_exp(e):
    # 简单表达式,直接返回(就是说,是啥返回啥)
    if is_basic_exp(e):
        return e

    op, a, b = e[0], eval_exp(e[1]), e[2]

    if op == "+":
        return eval_sum(a, b)
    if op == "-":
        return eval_sub(a, b)
    if op == "*":
        return eval_multi(a, b)
    if op == "/":
        return eval_div(a, b)
    else:
        raise ValueError("Unknow operation: {0}".format(op))


if __name__ == '__main__':
    # a = make_sum(3, make_div(10, 1))
    # print(a)

    a = eval_sum(10, 0)
    print(a)