def partition(nums, left, right):
    mid = nums[left]#初始化一个待比较数据
    i,j = left, right
    while(i < j):
        while(i<j and nums[j]>=mid): #从后往前查找，直到找到一个比mid更小的数
            j-=1
        nums[i] = nums[j] #将更小的数放入左边
        print("step1 nums is {0}, i is {1}".format(nums, i))
        while(i<j and nums[i]<=mid): #从前往后找，直到找到一个比mid更大的数
            i+=1
        nums[j] = nums[i] #将更大的数放入右边
        print("step2 nums is {0} i is {1}".format(nums, i))
    #循环结束，i与j相等
    nums[i] = mid #待比较数据放入最终位置
    print("finally nums is {0}".format(nums))
    print("i is {0}".format(i))
    return i #返回待比较数据最终位置

#快速排序
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

if __name__ == '__main__':

    # arr = [1,3,2,2,0]
    arr = [14,1,2,3, 15, 6, 7,22]
    # quicksort(arr, 0, 3)
    # print(arr)

    partition(arr, 0, 3)