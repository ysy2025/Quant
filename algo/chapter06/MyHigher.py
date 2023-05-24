def del_duplicated(input_list):
    temp = []
    for each in input_list:
        if each in temp:
            pass
        else:
            temp.append(each)
    return temp


def get_count(input_list):
    res = {}

    for each in input_list:
        if isinstance(each, (int, float)):
            res[each] = res.get(each, 0) + 1

    return res


from functools import lru_cache

@lru_cache()
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total - 2) + change_money(total - 3) + change_money(total - 5)


def show_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    row, col = 0, 0
    num, direction = 1, 0
    while num <= n ** 2:
        if matrix[row][col] == 0:
            matrix[row][col] = num
            num += 1
        if direction == 0:
            if col < n - 1 and matrix[row][col + 1] == 0:
                col += 1
            else:
                direction += 1
        elif direction == 1:
            if row < n - 1 and matrix[row + 1][col] == 0:
                row += 1
            else:
                direction += 1
        elif direction == 2:
            if col > 0 and matrix[row][col - 1] == 0:
                col -= 1
            else:
                direction += 1
        else:
            if row > 0 and matrix[row - 1][col] == 0:
                row -= 1
            else:
                direction += 1
        direction %= 4

    return matrix


class Parent:
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

if __name__ == '__main__':
    # a = change_money(99)
    # print(a)

    # b = show_spiral_matrix(4)
    # print(b)

    print(Parent.x, Child1.x, Child2.x)
    Child1.x = 2
    print(Parent.x, Child1.x, Child2.x)
    Parent.x = 3
    print(Parent.x, Child1.x, Child2.x)