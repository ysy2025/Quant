def quickSort(lst):
    if len(lst) <= 1:
        return lst

    mid = lst[0]
    left = [each for each in lst if each < mid]
    midNums = [each for each in lst if each == mid]
    right = [each for each in lst if each > mid]

    return quickSort(left) + midNums + quickSort(right)
if __name__ == '__main__':
    a = [{'e': 1, 'a': 1, 't': 1}, {'t': 1, 'e': 1, 'a': 1}, {'t': 1, 'a': 1, 'n': 1}, {'a': 1, 't': 1, 'e': 1},
         {'n': 1, 'a': 1, 't': 1}, {'b': 1, 'a': 1, 't': 1}]

    # b = sortDict(a)

    # print(b)

    b = [7,6,5,6,7,4,6,345,34,56,35]
    print(quickSort(b))