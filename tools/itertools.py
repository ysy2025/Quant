import itertools

if __name__ == '__main__':
    items = list("123")
    count = 0
    for item in itertools.permutations(items):
        print(item)
        count += 1
    print(count)

    """"
    permutations,排列,就是排列组合的排列
    combinations,组合,就是排列组合的组合
    combinations_with_replacement,不考虑顺序,有放回,相当于A
    product,笛卡尔积
    """

    """
    在量化中,通过参数组合来寻找最优参数时,一般都会使用笛卡尔积
    """