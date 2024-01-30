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

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i < right:
        print("now i is {0} index is {1} arr is {2}".format(i, index, arr))
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    print("now arr is {0}".format(arr))
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
if __name__ == '__main__':
    a = [5,4,3,2,7,2]
    # exchangOrder(a)
    # print(quickSort(a))
    b = [4,2,1,3]
    # partition(b, 0, 4)
    print(quickSort(b))