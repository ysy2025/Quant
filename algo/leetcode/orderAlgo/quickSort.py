# def partition(nums, left, right):
#     print("now nums is {0} left is {1} right is {2}".format(nums, left, right))
# 
#     # 多指针方法
#     # 第一个作为mid,区分
#     midNum = nums[left]
# 
#     i = left
#     j = right
# 
#     # 从第二个开始遍历
#     # 从左到右,判断二者移动是否相交,不想交,pass
#     while i < j:
#         # left 对应值小于midNum,一直向右
#         while nums[i] <= midNum:
#             i += 1
#         # 当right大于midNum,一直向左移动
#         while nums[j] > midNum:
#             j -= 1
# 
#         # 移动完毕,如果二者还没有相遇,比如这种 8,7,10,6,13 这种,交换10和6
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#             print("nums is {0}, i is {1}, j is {2}".format(nums, i, j))
#         # 然后继续移动
# 
#     # 彻底移动完毕后,左右肯定相遇了,交换 j对应值(-1后,在i+1的右边了)和midNum
#     nums[left] = nums[j]
#     nums[j] = midNum
#     print("最后了,nums is {0}, i is {1}, j is {2}".format(nums, i, j))
#     return j


def partition(nums,start,end):
    """
    用nums[start] 做基准值，在start到end这个范围进行分区
    """
    midNum = nums[start]

    while start < end :
        # 如果基准值和end范围最右边的值大于基准值，则，end-1，一直循环这个过程，直到start到end这个范围内最后一个大于基准值的值
        while start < end and nums[end] >= midNum:
            print("end 需要 降低")
            end -= 1
        nums[start] = nums[end]
        print("右边起的循环结束 nums is {0}, left is {1}, right is {2}".format(nums, start, end))
        # 如果基准值和end范围最左边的值小于基准值，则，start+1，一直循环这个过程，直到start到end这个范围内最后一个小于基准值的值
        while start < end and nums[start] <= midNum:
            print("start 需要增加")
            start += 1
        nums[end] = nums[start]
        print("左边起的循环结束 nums is {0}, left is {1}, right is {2}\n".format(nums, start, end))

    nums[start] = midNum
    print("\n整体的循环结束 nums is {0}, left is {1}, right is {2}".format(nums, start, end))
    return start

def quickSort(nums, left, right):
    # 特殊情况
    if len(nums) <= 1:
        return nums

    if left >= right:
        return

    index = partition(nums, left, right)
    # 快排左部
    quickSort(nums, left, index-1)
    # 快排右部
    quickSort(nums, index+1, right)

if __name__ == '__main__':
    a = [8,7,6,5,6,87,9,2,5,67]
    quickSort(a, 0, 9)

    print(a)