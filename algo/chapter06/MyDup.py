import random

def MyDup(input_list):
    count = {}

    for each in input_list:
        count[each] = count.get(each, 0) + 1

    # 得到Counter类似的功能
    res = []
    for key, value in count.items():
        if value <= 1:
            res.append(key)

    return res

if __name__ == '__main__':
    a = [random.randint(1, 1000) for each in range(100)]
    print(a)

    res = MyDup(a)
    print(res)