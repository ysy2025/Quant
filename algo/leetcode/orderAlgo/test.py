def exchangOrder(a):
    length = len(a)
    print("beginning a is {0}".format(a))
    index = 0
    for i in range(length-1):
        for j in range(i+1, length):
            print("i is {0} and a[i] is {1} j is {2} and a[j] is {3}".format(i, a[i], j, a[j]))
            index += 1
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                print("now a is {0}".format(a))

        print("index is {0}".format(index))


if __name__ == '__main__':
    a = [5,4,3,2,7,2]
    exchangOrder(a)